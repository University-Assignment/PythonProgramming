import math
import random

# 미션1: 팩토리얼 함수
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

num = int(input('팩토리얼을 구하고자 하는 정수값 입력 : '))
print('결과값 :', fact(num))

# 미션2: 소수찾기 함수
def get_primes(n):
    result = []
    for i in range(2, n + 1):
        isPrime = True;
        if i != 2 and i % 2 == 0:
            continue
        for j in range(3, int(math.sqrt(i)) + 1, 2):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            result.append(i)
    return result

num = int(input('정수 입력 : '))
print('1부터 %d까지의 소수 :' % num, get_primes(num))

# 미션3: 패스워드 생성기
def chaged_genPass():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    isSuccess = False
    while not isSuccess:
        password = ""
        for i in range(6):
            index = random.randrange(len(alphabet))
            add = alphabet[index]
            if index < 26:
                if random.randrange(2) == 0:
                    add = add.upper()
            else:
                isSuccess = True
            password = password + add
    return password

print(chaged_genPass())

# 미션4: 리스트에서 최소값 찾기
def find_minimum(list):
    minValue = list[0]
    for i in range(1, len(list)):
        if minValue > list[i]:
            minValue = list[i]
    return minValue

list = [7, 10, 3, 5, 2]
print('최소값 :', find_minimum(list))

# Zoom
def selection_sort(x):
    n = len(x)
    for i in range(n - 1):
        selValue = x[i]
        selIndex = i
        for j in range(i + 1, n):
            if x[j] < selValue:
                selValue = x[j]
                selIndex = j
        x[i], x[selIndex] = selValue, x[i]


list = [180, 165, 175, 170, 160, 171, 150, 162]
selection_sort(list)

print(list)