from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk, Image
from pytesseract import *
import pyttsx
import cv2
import time
import numpy as np
from queue import Queue
import operator

def openFile(type):
    types = (("텍스트 파일", "*.txt"), ("이미지 파일", "*.png"))
    fileName = askopenfilename(title="파일 열기", filetypes=(types[type], ))
    fileExtension = fileName[-4:]
    fileExtension = fileExtension.lower()
    if fileExtension == '.txt':
        readStr(fileName)
    elif fileExtension == '.jpg' or fileExtension == '.png':
        oepnImage(fileName)
    #countWord()

def readStr(fileName):
    string = ""
    f = open(fileName)
    index = 1
    for line in f.readlines():
        string += str(index) + '. ' + line
        index += 1
    text.delete(1.0, END)
    text.insert(1.0, string)

def ocr(lang='kor+eng'):
    global image
    if image is not None:
        string = ""
        result = image_to_string(image, lang=lang).replace('\n\n', '\n')
        text.delete(1.0, END)
        lines = result.split('\n')
        index = 1
        for line in lines:
            string += str(index) + '. ' + line + '\n'
            index += 1
        text.insert(1.0, string)

def oepnImage(fileName):
    global image
    global imageForm

    if imageForm is not None:
        imageForm.destroy()

    imageForm = Toplevel(window)
    image = Image.open(fileName)
    background = ImageTk.PhotoImage(image)
    label = Label(imageForm, image=background)
    label.image = background  # 참조
    label.pack()

def readText():
    string = getText()
    if string is not None:
        tts.say(string)
        tts.runAndWait()

def getText():
    string = text.get(1.0, END)
    split = string.split('\n')
    result = ""
    for s in split:
        result += s[3:] + "\n"
    return result

def countWord():
    table = dict()
    words = getText().replace('\n', ' ').split(' ')
    for word in words:
        if len(word) > 0:
            if word not in table:
                table[word] = 1
            else:
                table[word] += 1
    listbox.delete(0, END)
    for i, word in enumerate(table):
        listbox.insert(i, word + ' : ' + str(table[word]))

def useWebCAM():
    cap = cv2.VideoCapture(0)

    if cap.isOpened() == False:
        print("Unable to read camera")
    idx = 0
    while True:
        ret, img_ori = cap.read()
        if not ret:
            break
        h, w, c = img_ori.shape
        gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        img_thresh = cv2.adaptiveThreshold(gray, maxValue=255.0, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=19, C=9)
        img = Image.fromarray(img_thresh)
        global enclosure_queue
        if idx < 50:
            enclosure_queue.put(img)
            idx += 1
            print('찰칵')
        else:
            print('완료')
            break;
        cv2.imshow("name", img_thresh)

        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()

def readWebCAM():
    table = dict()
    while True:
        if not enclosure_queue.empty():
            data = enclosure_queue.get()
            string = image_to_string(data, lang='kor+eng').replace('\n\n', '\n')
            if len(string) > 0:
                words = string
                tempLine = 0
                if words not in table:
                    table[words] = 1
                else:
                    table[words] += 1
        else:
            break
    sortedTable = sorted(table.items(), key=operator.itemgetter(1), reverse=True)
    listbox.delete(0, END)
    for i, word in enumerate(sortedTable):
        listbox.insert(i, word)
        break


enclosure_queue = Queue()
image = None
imageForm = None

window = Tk()
tts = pyttsx.init()

menuBar = Menu(window)
file = Menu(menuBar, tearoff=0)
file.add_command(label="Text", command=lambda k=0: openFile(k))
file.add_command(label="Image", command=lambda k=1: openFile(k))
file.add_command(label="WebCAM", command=useWebCAM)
file.add_command(label="DrawingBoard")
menuBar.add_cascade(label="파일", menu=file)

func = Menu(menuBar, tearoff=0)
func.add_command(label="OCR", command=ocr)
func.add_command(label="TTS", command=readText)
func.add_command(label="맞춤법 검사")
func.add_command(label="맞춤법 자동 수정")
func.add_command(label="단어 카운터", command=countWord)
func.add_command(label="문자 카운터")
func.add_command(label="스페이스 카운터")
menuBar.add_cascade(label="기능", menu=func)

text = Text(window)
text.grid(row=0, column=0)

listbox = Listbox(window, selectmode='extended', height=0)
listbox.grid(row=0, column=1)

window.config(menu=menuBar)

window.mainloop()