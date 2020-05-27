from tkinter import *
import tkinter.font as font
from math import *
from random import *
import time

# 미션1: Tic-Tac-Toe 게임 만들기
def checked(i):
    global player
    button = list[i]

    if button["text"] != " ":
        return

    button["text"] = " " + player + " "
    button["bg"] = "yellow"

    if player == "X":
        player = "O"
        button["bg"] = "yellow"
    else:
        player = "X"
        button["bg"] = "lightgreen"

    winCase = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    for c in winCase:
        arr = [list[x]['text'] for x in c]
        if arr.count(' O ') == 3:
            Label(window, text='O 승리').grid(row=3, column=0)
        elif arr.count(' X ') == 3:
            Label(window, text='X 승리').grid(row=3, column=0)

window = Tk()
player = "X"
list = []

for i in range(9):
    b = Button(window, text=" ", width=5, command=lambda k=i: checked(k))
    b.grid(row=i // 3, column=i % 3)
    list.append(b)

window.mainloop()

# 미션2: 레이블과 버튼 배치
window = Tk()
colors = ['green', 'red', 'orange', 'white', 'yellow', 'blue']

for i in range(len(colors)):
    color = colors[i]
    Label(window, text=color, width=15, relief=RIDGE).grid(row=i, column=0)
    Button(window, width=15, bg=color).grid(row=i, column=1)

window.mainloop()

# 미션3: 스톱워치 만들기
def start():
    global flag
    flag = True


def stop():
    global flag
    flag = False


def run():
    if flag:
        global watch
        watch += 1
        time_label['text'] = str(watch)
    window.after(1000, run)


window = Tk()

flag = False
watch = 0

time_label = Label(window, text=str(watch), font=font.Font(size=100))
time_label.pack()

start = Button(window, text="시작", bg='yellow', command=start)
start.pack(fill=BOTH)
stop = Button(window, text="중지", bg='yellow', command=stop)
stop.pack(fill=BOTH)

run()
window.mainloop()

# 미션4: 간단한 계산기 만들기
def press(value):
    if value == 'C':
        number_entry.delete(0, "end")
    elif value == '=':
        exp = number_entry.get()
        number_entry.delete(0, "end")
        number_entry.insert(0, str("%.1f" % eval(exp)))
    else:
        number_entry.insert("end", value)

window = Tk()
window.title("간단한 계산기")

entry_value = StringVar(window, value='')

number_entry = Entry(window, textvariable=entry_value, width=36, bg='yellow')
number_entry.grid(row=0, columnspan=5)

buttons = [
    '7', '8', '9', '+', 'C',
    '4', '5', '6', '-', ' ',
    '1', '2', '3', '*', ' ',
    '0', '.', '=', '/', ' ']

for i in range(len(buttons)):
    button = buttons[i]
    c = lambda x=button: press(x)
    b = Button(window, text=button, width=6, command=c)
    b.grid(row=i // 5 + 1, column=i % 5)

window.mainloop()

# 미션5: 숫자 추측 게임
def setNumber():
    global number
    number = randint(1, 100)

def checkNumber():
    num = int(e1.get())
    if number == num:
        l2['text'] = '맞춤!'
    elif number < num:
        l2['text'] = '높음!'
    else:
        l2['text'] = '낮음!'


number = 0

setNumber()
window = Tk()
window.title("숫자를 맞춰보세요!")

l1 = Label(window, text="숫자 게임에 오신 것을 환영합니다!")
l2 = Label(window)
b1 = Button(window, text="시도", command=checkNumber, fg='green')
b2 = Button(window, text="초기화", command=setNumber, fg='red')
e1 = Entry(window)

l1.pack(padx=150)
e1.pack(side=LEFT)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
l2.pack(side=LEFT)

window.mainloop()