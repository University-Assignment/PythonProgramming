import turtle
import math
from random import randint

# Lab: 터틀 그래픽
t = turtle.Turtle()

while 0:
    dir = input('왼족=left, 오른쪽=right:')
    if dir == 'left':
        t.left(60)
        t.forward(50)
    elif dir == 'right':
        t.right(60)
        t.forward(50)

# Lab: 수하물 비용 계산
weight = int(input('짐의 무게는 얼마입니까? '))
if weight > 20:
    print('무거운 짐은 20,000원을 내셔야 합니다.')
else:
    print('짐에 대한 수수료는 없습니다.')
print('감사합니다')

# Lab | 미션1. 짝수 홀수 구분 프로그램
num = int(input('정수를 입력하시오: '))
if num % 2 == 0:
    print('입력된 정수는 짝수입니다.')
else:
    print('입력된 정수는 홀수입니다.')

# Lab | 미션2. 두수의 큰 수 출력
num1 = int(input('첫 번째 정수: '))
num2 = int(input('두 번째 정수: '))
if num1 > num2:
    print('큰 수는 ', num1)
else:
    print('큰 수는 ', num2)

# Lab | 미션3. 인터넷 할인 및 지불금액 출력
price = int(input('구입 금액을 입력하시오: '))
if price >= 100000:
    price = price * 0.95

print('지불 금액은 ', price, '입니다.')

# Lab | 미션4. 문자열의 중간문자
str = input('문자열을 입력하시오: ')
length = len(str)
if length % 2 == 0:
    print('중앙글자는 ', str[length // 2 - 1], str[length // 2])
else:
    print('중앙글자는 ', str[length // 2])

# Lab | 미션5. 졸업 학점 검사하기
credit = int(input('이수한 학점수를 입력하시오: '))
grade = float(input('평점을 입력하시오: '))
if credit >= 140 and grade >= 2.0:
    print('졸업 가능합니다!')
else:
    print('졸업이 힘듭니다!')

# Lab | 미션6. 음수, 0, 양수 구별하기
num = int(input('정수를 입력하시오: '))
if num > 0:
    print('입력된 정수는 양수입니다.')
elif num < 0:
    print('입력된 정수는 음수입니다.')
else:
    print('입력된 정수는 0입니다.')

# Lab | 미션7. 아이디 검사
userList = ['hong']

userId = input('아이디를 입력하시오: ')
if userId in userList:
    userPW = input('패스워드를 입력하시오: ')
    if userPW == '12345678':
        print('환영합니다.')
    else:
        print('잘못된 패스워드입니다.')
else:
    print('알 수 없는 사용자입니다!')

# Lab: 달의 일수 출력
month = int(input('월을 입력하시오:'))
if month == 2:
    print('월의 날수는 29일')
elif month == 4 or month == 6 or month == 10:
    print('월의 날수는 30일')
else:
    print('월의 날수는 31일')

# Lab: 윤년 판단
year = int(input('연도를 입력하시오: '))
if (year % 4 == 0 and year % 100 > 0) or year % 400 == 0:
    print(year, ' 년은 윤년입니다.')
else:
    print(year, ' 년은 윤년이 아닙니다.')

# 미션 8. 윤년 및 월의 일수 출력하기
year = int(input('연도를 입력하시오: '))
month = int(input('월을 입력하시오: '))
isLeapYear = False
day = 31

if (year % 4 == 0 and year % 100 > 0) or year % 400 == 0:
    isLeapYear = True

if month == 2:
    day = 28
elif month == 4 or month == 6 or month == 10:
    day = 30

if isLeapYear:
    if month == 2:
        day = 29
    print(year, ' 년은 윤년이며 월수는 ', day, '일입니다.')
else:
    print(year, ' 년은 평년이며 월수는 ', day, '일입니다.')

# Lab: 이차 방정식
A = float(input('A = '))
B = float(input('B = '))
C = float(input('C = '))

D = B ^ 2 - 4 * A * C

if A == 0:
    print('x = ', -C / B)
elif D == 0:
    print('x = ', -B / (2.0 * A))
elif D > 0:
    print('x1 = ', (-B + math.sqrt(D)) / 2.0 * A)
    print('x2 = ', (-B - math.sqrt(D)) / 2.0 * A)
else:
    print('실근이 존재하지 않음')

# Lab: 숫자 맞추기 게임
answer = randint(1, 100)
print('숫자 게임에 오신 것을 환영합니다.')
num = int(input('숫자를 맞춰 보세요: '))
if num == answer:
    print('사용자가 이겼습니다.')
elif num > answer:
    print('너무 큼!')
else:
    print('너무 작음!')
print('게임 종료')

# Lab: 가위 바위 보
player = input('(가위, 바위, 보) 중에서 하나를 선택하세요: ')
num = randint(0, 2)
playerWin = False

if num == 0:
    computer = '가위'
elif num == 1:
    computer = '바위'
else:
    computer = '보'
print('사용자: ', player, ' 컴퓨터: ', computer)

if player == computer:
    print('비겼음!')
elif player == '가위':
    if computer == '보':
        playerWin = True
elif player == '바위':
    if computer == '가위':
        playerWin = True
elif player == '보':
    if computer == '바위':
        playerWin = True

if playerWin:
    print('사용자가 이겼음!')
else:
    print('컴퓨터가 이겼음!')