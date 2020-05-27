import math
import turtle
from random import *

# 미션1: 화면에 거북이 그리기
win = turtle.Screen()
win.bgcolor('yellow')

t = turtle.Pen('turtle')
t.color('blue')

size = 20

for i in range(30):
    t.stamp()
    size += 3
    t.forward(size)
    t.right(24)
    
# 미션2: 동그라미 그리기
t = turtle.Turtle()
t.circle(50)

# 미션3: 팩토리얼 값 구하기 
# 오버플로우가 발생을 안합니다 ㅠㅠ
num = int(input('팩토리얼의 값을 입력하시오: '))
i = 1
fac = 1

while i <= num:
    fac *= i
    i += 1
print('%d!은 %d입니다.' % (num, fac))

# 미션4: 최대공약수 계산하기
x = int(input('첫 번째 수를 입력하시오: '))
y = int(input('두 번째 수를 입력하시오: '))

if y > x:
    temp = x
    x = y
    y = temp

while y > 0:
    r = x % y
    x = y
    y = r

print('최대 공약수는 %d 입니다.' % x)

# 미션5: 계좌번호 처리하기
acc = input('계좌번호를 입력하시오 : ')

for c in acc:
    if c != '-':
        print(c, end='')
print()

# 미션6: 주사위의 합 확률
sumList = []
for i in range(13):
    sumList.append(0)

count = int(input('주사위 실험 반복횟수: '))

for i in range(count):
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    sumList[dice1 + dice2] += 1

for i in range(2, 13):
    print(i, sumList[i])

# 미션7: 파이 계산
n = int(input('반복횟수를 입력하시오: '))

inside = 0
for i in range(n):
    x = random()
    y = random()
    if math.sqrt(x*x+y*y) <= 1:
        inside += 1

Pi = 4 * inside / n
print(Pi)

# Lab: 정수들의 합
sum = 0;
n = int(input('어디까지 계산할까요: '))

for i in range(1, n + 1):
    sum += i

print('1부터 %d 까지의 정수의 합 = %d' % (n, sum))

# Lab: 팩토리얼 계산
result = 1
n = int(input('정수를 입력하시오: '))

for i in range(1, n + 1):
    result *= i

print('%d!은 %d 이다.' % (n, result))

# Lab: 화면에 별 그리기
star = turtle.Turtle()

for i in range(5):
    star.forward(50)
    star.right(144)

# Lab: 화면에 다각형 그리기
polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

# Lab: 화면에 사각형 그리기
t = turtle.Turtle()
colors = ['yellow', 'red', 'purple']

for i in range(3):
    turtle.left(20)
    turtle.pencolor(colors[i])
    for j in range(4):
        turtle.forward(50)
        turtle.left(90)


# Lab: 함수 그래프 그리기
t = turtle.Turtle()
t.pendown()
for angle in range(360):
    y = math.sin(math.radians(angle))
    scaledX = angle
    scaledY = y * 100
    t.goto(scaledX, scaledY)
t.penup()

# Lab: 0~9까지 출력하기
i = 0
while i < 10:
    print(i, end=' ')
    i += 1

# Lab: (1+2+3+...+9+10) 계산하기
i = 1
sum = 0

while i <= 10:
    sum += i
    i += 1
print('합계= ', sum)

# Lab: 팩토리얼 계산
i = 1
fac = 1

while i <= 10:
    fac *= i
    i += 1
print('10!은 %d입니다.' % fac)

# Lab: 구구단 출력
i = 1
while i <= 9:
    print('3*%d = %d' % (i, i * 3))
    i += 1

# Lab: 자리수의 합
num = 1234
sum = 0

while num > 0:
    sum += num % 10
    num = num // 10

print('자리수의 합은 %d입니다.' % sum)


