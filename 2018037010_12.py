# 미션1: Sportscar 클래스
class Car:
    def __init__(self, speed):
        self.speed = speed

def setSpeed(self, speed):
    self.speed = speed

class SportsCar(Car) :
    def __init__(self, speed, turbo):
        super().__init__(speed)
        self.turbo = turbo

    def setTurbo(self, turbo):
        self.turbo=turbo

sc = SportsCar(200, True)
sc.setTurbo(False)

# 미션2: 도형
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return 0

    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

r = Rectangle(0, 0, 100, 200)
print("사각형의 면적", r.area())
print("사각형의 둘레", r.perimeter())

# 미션3: 학생과 강사
class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Student(Person):
    def __init__(self, name, number, studentType):
        super().__init__(name, number)
        self.studentType = studentType
        self.gpa = 0
        self.classes = []

    def enrollCourse(self, course):
        self.classes.append(course)

    def __str__(self):
        return "\n이름=" + self.name + "\n주민번호="+self.number + "\n수강과목=" + str(self.classes) + "\n평점="+str(self.gpa)

class Teacher(Person):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.courses = []
        self.salary = 3000000

    def assignTeaching(self, course):
        self.courses.append(course)

    def __str__(self):
        return "\n이름="+self.name + "\n주민번호="+self.number + "\n강의과목="+str(self.courses) + "\n월급=" + str(self.salary)

hong = Student("홍길동", "12345678", 0)
hong.enrollCourse("자료구조")
print(hong)

kim = Teacher("김철수", "123456790")
kim.assignTeaching("Python")
print(kim)

# 미션4: 은행 계좌
class BankAccount:
    def __init__(self, name, number, balance):
        self.balance = balance
        self.name = name
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self,  name, number, balance,  interest_rate):
        super().__init__( name, number, balance)
        self.interest_rate =interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self,  name, number, balance):
        super().__init__( name, number, balance)
        self.withdraw_charge = 10000

    def withdraw(self, amount):
        return BankAccount.withdraw(self, amount + self.withdraw_charge)

a1 = SavingsAccount("홍길동", 123456, 10000, 0.05)
a1.add_interest()
print("저축예금의 잔액=", a1.balance)

a2 = CheckingAccount("김철수", 123457, 2000000)
a2.withdraw(100000)
print("당좌예금의 잔액=", a2.balance)

# 미션5: 직원과 매니저
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus =bonus

    def getSalary(self):
        salary = super().getSalary()
        return salary + self.bonus

    def __repr__(self):
        return "이름: " + self.name + "; 월급: "+ str(self.salary) + "; 보너스: " + str(self.bonus)

kim = Manager("김철수", 2000000, 1000000)
print(kim)

# 미션6: Vehicle와 Car, Truc
class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        pass

    def stop(self):
        pass

class Car(Vehicle):
    def drive(self):
        return '승용자를 운전합니다. '
    def stop(self):
        return '승용자를 정지합니다. '

class Truck(Vehicle):
    def drive(self):
        return '트럭을 운전합니다. '

    def stop(self):
        return '트럭을 정지합니다. '

cars = [Truck('truck1'), Truck('truck2'),  Car('car1')]
for car in cars:
    print( car.name + ': ' + car.drive())

# 미션7: Card와 Deck
class Card:
    suitNames = ['클럽', '다이아몬드', '하트', '스페이드']
    rankNames = [None, '에이스', '2', '3', '4', '5', '6', '7', '8', '9', '10', '잭', '퀸', '킹']
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return Card.suitNames[self.suit] + " " + Card.rankNames[self.rank]

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        lst = [str(card) for card in self.cards]
        return str(lst)

deck = Deck()
print(deck)