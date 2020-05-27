import random

# 미션1: 키를 이용한 정렬 예제
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return repr('<이름: %s, 나이: %d>' % (self.name, self.age))

addressBook = [
    Person('최자영', 38),
    Person('김철수', 35),
    Person('홍길동', 20)
]

addressBook.sort(key=lambda address: address.age)
print(addressBook)

# 미션2: 피보나치 이터레이터
class FibIterator:
    def __init__(self, a=1, b=0, maxValue=50):
        self.a = a
        self.b = b
        self.maxValue = maxValue

    def __iter__(self):
        return self

    def __next__(self):
        n = self.a + self.b
        if n > self.maxValue:
            raise StopIteration()
        self.a = self.b
        self.b = n
        return n

for i in FibIterator():
    print(i, end=" ")
print()

# 미션3: 동전 던기지 게임
arr = ["head", "tail"]

while True:
    answer = input("동전 던지기를 계속하시겠습니까?(yes, no) ")
    if answer == 'no' or (not answer == 'no' and not answer == 'yes'):
        break
    print(random.choice(arr))