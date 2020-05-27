from math import *
import turtle

## 미션 1. 자기소개 출력
print('안녕하세요? 여러분')
print('저는 파이썬을 무척 좋아합니다.')
print('9*8은 ', 9 * 8, ' 입니다')
print('안녕히 계세요.')

## 미션 1. 간단한 숫자 맞추기 게임
number = 62
print('숫자게임에 오신 것을 환영합니다')
guess = int(input('1부터 100 사이의 숫자를 추측해보세요 : '))
if guess == number:
    print('맞았습니다.')
else:
    print('틀렸습니다')
print('게임이 종료되었습니다.')

## 미션 2. 자신의 영어 이니셜 쓰기
t = turtle.Turtle()
t.right(45)
t.forward(40)
t.left(90)
t.forward(40)
t.back(40)
t.right(135)
t.forward(50)

t.penup()
t.setposition(90, 0)
t.pendown()
t.left(90)
t.forward(50)
t.back(25)
t.right(90)
t.forward(60)
t.right(180)
t.circle(20, -180)

t.penup()
t.setposition(180, 0)
t.pendown()
t.forward(80)
t.back(40)
t.left(90)
t.forward(40)
t.left(90)
t.back(40)
t.forward(80)

# Lab | 미션 1 : 파티 준비
people = int(input('참석자의 수를 입력하시오: '))
chicken = people
beer = people * 2
cake = people * 4
print('치킨의 수: ', chicken)
print('맥주의 수: ', beer)
print('케익의 수: ', cake)

# Lab | 미션 2 : 변수 값 교환
x = 10
y = 20
x, y = y, x
print(x, y)

# Lab: 함수 값 계산
x = 2.0
y = 3.0 * x**2 + 7.0 * x + 9.0
print(y)

# Lab | 미션 3 : 감자 재배
potato = 20
potato += 30 * 52
potato -= 3 * 365
print(potato)

# Lab | 미션 4 : 복리 계산
money = 24
r = 0.06
n = 382
finalValue = money * (1 + r)**n
print(finalValue)

# Lab | 미션 5 : 등산 시간 계산
time = 0
time += 10 / 20
height = sqrt(3**2 + 4**2)
time += height / 10
time += height / 30
time += 8 / 20
print(time)

# Lab | 미션 6 : 구의 부피 계산하기
r = 5.0
volume = 4.0 / 3.0 * 3.141592 * r**3
print(volume)

# Lab | 미션 7 : 별까지 거리 계산하기
speedOfLight = 2.907925 * 10**5
distance = 40 * 10**12
sec = distance / speedOfLight
year = sec / (60.0 * 60.0 * 24.0 * 365.0)
print(year)

# Lab: 대화하는 프로그램 만들기
name = input('이름을 입력해주세요 : ')
print(name, '님 만나서 반값습니다.')
age = int(input('나이를 입력해주세요 : '))
print('10년 후면', age + 10, '살이 되시는군요!')

# Lab | 미션 8 : 자동판매기 프로그램
price = int(input('물건 값을 입력하시오 : '))
nMoney1000 = int(input('1000원 지폐개수 : '))
nMoney500 = int(input('500원 동전개수 : '))
nMoney100 = int(input('100원 동전개수 : '))

change = nMoney1000 * 1000 + nMoney500 * 500 + nMoney100 * 100 - price

nCoin500 = change // 500
change %= 500

nCoin100 = change // 100
change %= 100

nCoin10 = change // 10
change %= 10

nCoin1 = change

print('500원=', nCoin500, '100원=', nCoin100, '10원=', nCoin10, '1원=', nCoin1)

# Lab: 약자로 만들기
word1 = input('첫 번째 단어를 입력해주세요 : ')
word2 = input('두 번째 단어를 입력해주세요 : ')
word3 = input('세 번째 단어를 입력해주세요 : ')

acronym = word1 + word2 + word3

print(acronym)