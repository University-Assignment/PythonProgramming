from tkinter import *
from tkinter.filedialog import *
from PIL import Image
from pytesseract import *
import pyttsx
import cv2
import time

def openFile():
    fileName = askopenfilename(title="파일 열기", filetypes=(("텍스트 파일", "*.txt"), ("이미지 파일", "*.png")))
    fileExtension = fileName[-4:]
    fileExtension = fileExtension.lower()
    if fileExtension == '.txt':
        readStr(fileName)
    elif fileExtension == '.jpg' or fileExtension == '.png':
        toStr(fileName)
    countWord()

def readStr(fileName):
    string = ""
    f = open(fileName)
    for line in f.readlines():
        string += line
    text.delete(1.0, END)
    text.insert(1.0, string)

def toStr(fileName, lang='kor+eng'):
    img = Image.open(fileName)
    string = image_to_string(img, lang=lang).replace('\n\n', '\n')
    text.delete(1.0, END)
    text.insert(1.0, string)

def readText():
    string = text.get(1.0, END)
    if string != None:
        tts.say(string)
        tts.runAndWait()

def countWord():
    string = text.get(1.0, END)
    table = dict()
    words = string.replace('\n', ' ').split(' ')
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

    while True:
        ret, img_ori = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        img = Image.fromarray(thresh)
        cv2.imshow("name", thresh)
        string = image_to_string(img, lang='kor+eng').replace('\n\n', '\n')
        print(string)
        #if len(string) > 0:
            #text.delete(1.0, END)
            #text.insert(1.0, string)
            #break

        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()

window = Tk()
tts = pyttsx.init()

menu = Menu(window)
menu.add_cascade(label="파일 열기", command=openFile)
menu.add_cascade(label="Text 읽기", command=readText)
menu.add_cascade(label="WebCAM 사용", command=useWebCAM)

text = Text(window)
text.pack(side=LEFT)

listbox = Listbox(window, selectmode='extended', height=0)
listbox.pack()

window.config(menu=menu)

window.mainloop()