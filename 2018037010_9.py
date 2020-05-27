# 미션1: 자동차 클래스 작성
class Car:
    def __init__(self, speed=0, gear=1, color="white", efficiency=0):
        self.__speed = speed
        self.__gear = gear
        self.__color = color
        self.__efficiency = efficiency;

    def getSpeed(self):
        return self.__speed;

    def setSpeed(self, speed):
        self.__speed = speed;

    def getGear(self):
        return self.__gear;

    def setGear(self, gear):
        self.__gear = gear;

    def getColor(self):
        return self.__color;

    def setColor(self, color):
        self.__color = color;

    def getEfficiency(self):
        return self.__efficiency;

    def setEfficiency(self, efficiency):
        self.__efficiency = efficiency;

    def getFuel(self, distance):
        return distance / self.__efficiency;

    def __str__(self):
        return '(%d, %d, %s, %s)' % (self.__speed, self.__gear, self.__color, self.__efficiency)

myCar = Car()
myCar.setGear(3);
myCar.setSpeed(100);
print(myCar)

myCar2 = Car(100, 3, 'white', 8)
print(myCar2.getFuel(16))
print(myCar2)

# 미션2: 연락처 클래스 작성
'''ContactInfo 라는 연락처 클래스를 작성해보자. 단 다음의 요구사항을 따라 작성한다
– 속성 : name, age, email, phone, address
– 메소드 : 속성에 대한 getters, setters 작성
– 생성자는 name, age, email, phone, address 를 파라메터로 하고, 이를 초기화할 수 있도록 한다. '''
class ContactInfo:
    def __init__(self, name, age, email, phone, address):
        self.__name = name;
        self.__age = age;
        self.__email = email;
        self.__phone = phone;
        self.__address = address;

    def getName(self):
        return self.__name;

    def setName(self, name):
        self.__name = name;

    def getAge(self):
        return self.__age;

    def setAge(self, age):
        self.__age = age;

    def getEmail(self):
        return self.__email;

    def setEmail(self, email):
        self.__email = email;

    def getPhone(self):
        return self.__phone;

    def setPhone(self, phone):
        self.__phone = phone;

    def getAddress(self):
        return self.__addresss;

    def setAddress(self, address):
        self.__address = address;


# 줌
class Game:
    bossPower = 5000
    count = 0

    def __init__(self, name=None, power=0):
        self.__name = name
        self.__power = power

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getPower(self):
        return self.__power

    def setPower(self, power):
        self.__power = power

    def attack(self, power):
        self.bossPower -= power
        self.count += 1
        if self.bossPower < 0:
            print(self.__name, "가 우승", self.count, "번을 공격했습니다.")
            return True
        return False


unit1 = Game("unit1", 100)
unit2 = Game("unit2", 100)

while (1):
    if unit1.attack(unit1.getPower()):
        break
    if unit2.attack(unit2.getPower()):
        break
