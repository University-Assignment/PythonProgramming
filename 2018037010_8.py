'''from cs1media import *

# 미션1: 이미지 반전 프로그램
img = load_picture("img.jpg")
w, h = img.size()
for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)
        r, g, b = 255-r, 255-g, 255-b
        img.set(x, y, (r, g, b))
img.show()

# 미션2: 이미지를 흑백으로 반전시키기
threshold = 150
white = (255, 255, 255)
black = (0, 0, 0)

img = load_picture("img.jpg")
w, h = img.size()
for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)
        v = (r + g + b)
        if v >= threshold:
            img.set(x, y, white)
        else:
            img.set(x, y, black)
img.show()

# 미션3: 회문 검사하기
s = input("문자열을 입력하시오: ")
s = s.replace(" ", "")
if s == ''.join(reversed(s)):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")

# 미션4: 단어 카운터
fname = input("파일 이름: ")
file = open(fname, "r")
table = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in table:
            table[word] = 1
        else:
            table[word] += 1
print(table)

for a in table:
    print(a, ":", "*" * int(table[a]))

# 미션5: 축약어 만들기
table = { "B4": "Before",
          "TX": "Thanks",
          "BBL": "Be Back Later",
          "BCNU":"Be Seeing You",
          "HAND":"Have A Nice Day" }

message = input('번역할 문장을 입력하시오: ')
words = message.split()
result = ""
for word in words:
    if word in table:
        result += table[word] + " "
    else:
        result += word
print(result)

# 미션6: csv 파일로부터 딕셔너리로
tip = dict()
key = []
f = open("tip.csv", "r")
for line in f.readlines():
    info = line.strip('\n').split(',')
    if len(key) == 0:
        for i in range(len(info)):
            key.append(info[i])
            tip[info[i]] = []
    else:
        for i in range(len(info)):
            tip[key[i]].append(info[i])

print(tip)'''


import math
import numpy as np
import matplotlib.pyplot as plt
'''
# 1
num = [0, ] * 3

num[0], num[1], num[2] = map(int, input('숫자 3개를 입력하시오 : ').split())
count = len(num)
average = sum(num) / count
variance = 0;
for i in range(count):
    variance += math.pow(num[i] - average, 2.0)
variance = variance / count

print("%d 평균", average)
print("%d 표준편차", math.sqrt(variance))

#2
x = np.arange(16)
x = x.reshape(4, 4)

a, b, c, d = x[:2, :2], x[2:, :2], x[:2, 2:], x[2:, 2:]
print(a, b, c, d, sep='\n')


#3
t = np.arange(-1, 1, 1 / 20000)
s = np.cos(10 * np.pi * t) + 0.5 * np.cos(2 * np.pi * t) * np.cos(10 * np.pi * t)
plt.plot(t, s)
plt.show()

# b 주기 = 1s
'''
#4
# 10, 에러
