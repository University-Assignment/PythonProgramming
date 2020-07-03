from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk, Image
from pytesseract import *
import pyttsx3
import cv2
from queue import Queue
import operator
import requests
import json
from threading import Thread
import socket
from _thread import *

class Network: # 서버와 통신을 위한 클래스
    # 접속할 서버의 ip와 port 설정
    HOST = '127.0.0.1'
    PORT = 1319

    def __init__(self, form):
        # 접속하고 스레드를 킴
        self.form = form
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        start_new_thread(self.threaded, ())

    def readInt(self): # 바이트 배열 형태의 패킷을 정수로 읽음
        data = self.client_socket.recv(4);
        if not data:
            return None
        value = int.from_bytes(data, "little");
        return value

    def writePacket(self, header, params): # header(종류), 문자열 길이, 문자열 순서로 패킷을 보냄
        data = params.encode();
        length = len(data);
        self.client_socket.sendall(header.to_bytes(4, byteorder='little'));
        self.client_socket.sendall(length.to_bytes(4, byteorder='little'));
        self.client_socket.sendall(data);

    def threaded(self): # 서버와 연결되어 지속적으로 패킷을 받아오는 스레드
        global accountForm
        while True:
            try:
                header = self.readInt(); # 어떤 종류의 패킷인지 구분
                if header == 0: # 회원가입 결과
                    result = self.readInt()
                    self.form.registerResult(result == 1) # 결과에 따라 맞는 기능 작동
                    pass
                elif header == 1: # 로그인 결과
                    result = self.readInt()
                    self.form.loginResult(result == 1) # 결과에 따라 맞는 기능 작동
                    pass
            except ConnectionResetError as e:

                print('Disconnected')
                break
            except:
                continue

        # 닫음
        self.client_socket.close()
        sys.exit(1)

class AccountForm: # 계정인증창 클래스

    def __init__(self): # 계정인증창을 뜨게하고 서버에 연결 시도
        self.loginSuccess = False
        self.window = Tk()
        self.network = Network(self)

        Label(self.window, text='아이디').grid(row=0)
        Label(self.window, text='비밀번호').grid(row=1)

        self.e1 = Entry(self.window)
        self.e2 = Entry(self.window)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

        Button(self.window, text='회원가입', command=self.register).grid(row=3, column=0, sticky=W, pady=4)
        Button(self.window, text='로그인', command=self.login).grid(row=3, column=1, sticky=W, pady=4)

        self.window.mainloop()

    def isLoginSuccess(self): # 로그인 성공인지 실패인지 확인
        return self.loginSuccess

    def registerResult(self, success): # 회원가입 결과 표출
        if not success:
            form = Toplevel(self.window)
            Label(form, text='존재하는 아이디입니다.').pack()
            self.window.after(1000, form.destroy)

    def loginResult(self, success): # 로그인 결과 표출
        if success:
            self.loginSuccess = True
            self.window.destroy()
        else:
            form = Toplevel(self.window)
            Label(form, text='로그인 실패').pack()
            self.window.after(1000, form.destroy)

    def register(self): # 회원가입 시도 (서버로 패킷을 보냄)
        id = self.e1.get()
        pw = self.e2.get()
        self.network.writePacket(0, id + ";" + pw)

    def login(self): # 로그인 시도 (서버로 패킷을 보냄)
        id = self.e1.get()
        pw = self.e2.get()
        self.network.writePacket(1, id + ";" + pw)

class Spelling: # 맞춤법 확인 및 수정 기능이 담긴 클래스
    def __init__(self): # 기능을 구현하는데 필요한 값들 선언
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ko; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 IPMS/A640400A-14D460801A1-000000426571',
        }
        self.url = "https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy"
        self.params = {
            '_callback': 'jQuery112405367619129812142_1591163584648',
            'q': '',
            'where': 'nexearch',
            'color_blindness': 0,
            '_': 1591163584650
        }

    def checkSpelling(self, text): # 크롤링을 통해 맞춤법이 맞는지 확인
        self.params['q'] = text
        response = requests.get(self.url, headers=self.headers, params=self.params).text
        response = response.replace(self.params['_callback'] + '(', '')
        response = response.replace(');', '')
        response_dict = json.loads(response)
        errorCount = response_dict['message']['result']['errata_count']
        result_text = response_dict['message']['result']['origin_html']
        result_text = result_text.replace("<span class='result_underline'>", "").replace("<br>", "")
        result_text = re.sub(r'<\/?.*?> ', '|', result_text)
        result_text = re.sub(r'<\/?.*?>', '|', result_text)
        return (errorCount, result_text)

    def modifySpelling(self, text): # 크롤링을 통해 맞는 맞춤법을 가져와 수정
        self.params['q'] = text
        response = requests.get(self.url, headers=self.headers, params=self.params).text
        response = response.replace(self.params['_callback'] + '(', '')
        response = response.replace(');', '')
        response_dict = json.loads(response)
        result_text = response_dict['message']['result']['notag_html']
        result_text = re.sub(r'<\/?.!br?>', '', result_text)
        lines = result_text.split('<br>')
        return lines

class MainForm: # 메인창 클래스
    def __init__(self): # 로그인 성공시 메인창을 뜨게함
        self.queue = Queue()
        self.image = None
        self.imageForm = None
        self.background = None
        self.curOption = 1
        self.label_ = None

        self.window = Tk()

        # 기능 구현에 사용할 것들
        self.tts = pyttsx3.init()
        self.spelling = Spelling()

        # 메뉴 생성
        menuBar = Menu(self.window)
        file = Menu(menuBar, tearoff=0)
        file.add_command(label="Text", command=lambda k=0: self.openFile(k))
        file.add_command(label="Image", command=lambda k=1: self.openFile(k))
        file.add_command(label="WebCAM", command=self.useWebCAM)
        menuBar.add_cascade(label="파일", menu=file)

        func = Menu(menuBar, tearoff=0)
        func.add_command(label="OCR", command=self.ocr)
        func.add_command(label="TTS", command=self.readText)
        func.add_command(label="맞춤법 검사", command=lambda k=False: self.excute(k))
        func.add_command(label="맞춤법 자동 수정", command=lambda k=True: self.excute(k))
        func.add_command(label="단어 카운터", command=self.countWord)
        func.add_command(label="문자 카운터", command=self.countChar)
        func.add_command(label="스페이스 카운터", command=self.countSpace)
        func.add_command(label="저장", command=self.save)
        menuBar.add_cascade(label="기능", menu=func)

        self.var1 = IntVar(value=1)
        cb1 = Checkbutton(self.window, text='줄 번호', variable=self.var1, onvalue=1, offvalue=0, command=self.reload)
        cb1.pack(side=TOP, anchor='nw')

        self.text = Text(self.window)
        self.text.pack(side=LEFT)

        scrollbar = Scrollbar(self.window)
        scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(self.window, selectmode='extended', yscrollcommand=scrollbar.set)
        self.listbox.pack(side=LEFT, fill="y")

        scrollbar["command"] = self.listbox.yview

        self.window.config(menu=menuBar)

        self.window.mainloop()

    def excute(self, apply): # 맞춤법 검사 및 자동 수정 함수
        if apply:
            lines = self.spelling.modifySpelling(self.getText())
            index = 1
            string = ""
            # 수정된 튜플 형태의 텍스트를 문자열로 바꾸어줌 (줄 번호 표시가 활성화되어 있으면 줄 번호를 표시함)
            for line in lines:
                if len(line) > 0:
                    if self.var1.get() == 1:
                        string += str(index) + '. ' + line + '\n'
                        index += 1
                    else:
                        string += line + '\n'
            # 원래 있던 내용을 지우고 새로 써줌
            self.text.delete(1.0, END)
            self.text.insert(1.0, string)
        else:
            errorCount, result_text = self.spelling.checkSpelling()
            self.listbox.delete(0, END)
            self.listbox.insert(0, '틀린갯수 : ' + str(errorCount))
            split = result_text.split('|')
            # 리스트박스에 틀린 부분들을 순서대로 넣어줌
            for i, word in enumerate(split):
                if word is not '':
                    self.listbox.insert(i + 1, word)


    def openFile(self, type): # 파일을 여는 함수
        types = (("텍스트 파일", "*.txt"), ("이미지 파일", "*.png"))
        fileName = askopenfilename(title="파일 열기", filetypes=types[type:])
        fileExtension = fileName[-4:]
        fileExtension = fileExtension.lower()
        if fileExtension == '.txt':
            self.readStr(fileName)
        elif fileExtension == '.jpg' or fileExtension == '.png':
            self.oepnImage(fileName)


    def readStr(self, fileName): # 텍스트에서 글을 읽는 함수
        string = ""
        f = open(fileName)
        index = 1
        for line in f.readlines():
            if len(line) > 0:
                if self.var1.get() == 1:
                    string += str(index) + '. ' + line
                    index += 1
                else:
                    string += line + '\n'
        self.text.delete(1.0, END)
        self.ext.insert(1.0, string)
        self.curOption = self.var1.get()


    def ocr(self, lang='kor+eng'): # 이미지에서 글을 ocr을 통해 읽는 함수
        if not self.queue.empty():
            self.readWebCAM()

        if self.image is not None:
            string = ""
            result = image_to_string(self.image, lang=lang).replace('\n\n', '\n')
            self.text.delete(1.0, END)
            lines = result.split('\n')
            index = 1
            for line in lines:
                if len(line) > 0:
                    if self.var1.get() == 1:
                        string += str(index) + '. ' + line + '\n'
                        index += 1
                    else:
                        string += line + '\n'
            self.text.insert(1.0, string)
            self.curOption = self.var1.get()


    def reload(self): # 줄의 표현 유무를 재설정
        lines = self.getText().split('\n')
        string = ""
        self.text.delete(1.0, END)
        index = 1
        for line in lines:
            if len(line) > 0:
                if self.var1.get() == 1:
                    string += str(index) + '. ' + line + '\n'
                    index += 1
                else:
                    string += line + '\n'
        self.text.insert(1.0, string)
        self.curOption = self.var1.get()


    def oepnImage(self, fileName): # 이미지를 열고 새로운 창을 열어 표출하는 함수
        '''
        if self.imageForm is not None:
            self.imageForm.destroy()

        self.imageForm = Toplevel(self.window)
        '''
        self.image = Image.open(fileName)
        '''
        self.background = ImageTk.PhotoImage(self.image)
        self.label_ = Label(self.imageForm, image=self.background)
        self.label_.image = self.background  # 참조
        self.label_.pack()'''


    def readText(self): # tts를 통해 텍스트를 읽어주는 함수
        string = self.getText()
        if string is not None:
            def speak():
                self.tts.say(string)
                self.tts.runAndWait()
            Thread(target=speak).start()


    def getText(self): # 현재 test를 읽어오는 함수
        result = str()
        string = self.text.get(1.0, END)
        if string is '\n':
            return result
        split = string.split('\n')
        for s in split:
            if len(s) > 0:
                if self.curOption == 1:
                    result += s[3:] + "\n"
                else:
                    result += s + "\n"
        return result


    def countWord(self): # 단어수를 세어주는 함수
        table = dict()
        words = self.getText().replace('\n', ' ').split(' ')
        for word in words:
            if len(word) > 0:
                if word not in table:
                    table[word] = 1
                else:
                    table[word] += 1
        self.listbox.delete(0, END)
        for i, word in enumerate(table):
            self.listbox.insert(i, word + ' : ' + str(table[word]))


    def countChar(self): # 문자 수를 세어주는 함수
        table = dict()
        chars = self.getText().replace('\n', ' ')
        for char in chars:
            if char is not ' ':
                if char not in table:
                    table[char] = 1
                else:
                    table[char] += 1
        self.listbox.delete(0, END)
        for i, word in enumerate(table):
            self.listbox.insert(i, word + ' : ' + str(table[word]))


    def countSpace(self): # 띄어쓰기의 수를 세어주는 함수
        count = 0
        chars = self.getText()
        for char in chars:
            if char is ' ':
                count += 1
        self.listbox.delete(0, END)
        self.listbox.insert(0, '스페이스 : ' + str(count))


    def useWebCAM(self): # 웹캠을 이용해 사진을 찍어주는 함수
        cap = cv2.VideoCapture(0)

        if cap.isOpened() == False:
            print("Unable to read camera")
        idx = 0
        while True:
            ret, img_ori = cap.read()
            if not ret:
                break
            h, w, c = img_ori.shape
            # 흑백으로 바꾸고
            gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
            # 인식률을 높이기 위해 구분을 더욱 잘되게 해주고
            gray = cv2.GaussianBlur(gray, (5, 5), 0)
            img_thresh = cv2.adaptiveThreshold(gray, maxValue=255.0, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                               thresholdType=cv2.THRESH_BINARY, blockSize=19, C=9)

            # 배열 형태에서 이미지로 읽어옴
            img = Image.fromarray(img_thresh)

            # 50장 찍어서 큐에 담음
            if idx < 50:
                self.queue.put(img)
                idx += 1
            else:
                break;
            # 현재 웹캠에 보이는 화면 표출
            cv2.imshow("name", img_thresh)
            # q누르면 종료
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break

        #자원 해제 및 창 닫기
        cap.release()
        cv2.destroyAllWindows()


    def readWebCAM(self): # 웹캠으로 찍은 사진을 ocr을 통해 글로 읽는 함수
        table = dict()
        while True:
            if not self.queue.empty():
                data = self.queue.get()
                string = image_to_string(data, lang='kor+eng').replace('\n\n', '\n')
                if len(string) > 0:
                    words = string
                    if words not in table:
                        table[words] = 1
                    else:
                        table[words] += 1
            else:
                break
        #많은 것 부터 적은 것으로 정렬
        sortedTable = sorted(table.items(), key=operator.itemgetter(1), reverse=True)
        self.listbox.delete(0, END)
        for i, word in enumerate(sortedTable):
            self.listbox.insert(i, word)
            break


    def save(self): # 수정된 텍스트를 저장하는 함수
        f = asksaveasfile(mode='w', defaultextension=".txt", filetypes=(("텍스트 파일", "*.txt"),))
        if f is None:
            return
        text2save = self.getText()
        f.write(text2save)
        f.close()

if __name__ == '__main__':

    accountForm = AccountForm()
    if accountForm.isLoginSuccess():
        MainForm()
