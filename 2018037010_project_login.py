from tkinter import *

window = Tk()
Label(window, text='아이디').grid(row=0)
Label(window, text='비밀번호').grid(row=1)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(window, text='회원가입').grid(row=3, column=0, sticky=W, pady=4)
Button(window, text='로그인').grid(row=3, column=1, sticky=W, pady=4)

window.mainloop()
