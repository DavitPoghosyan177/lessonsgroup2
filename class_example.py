#!/usr/bin/python3
class Car:
    def __init__(self , model = "", age = 0 , horse_power = 0):
        self.model = model
        self.age = age
        self.horse_power = horse_power
    def __repr__(self):
        return str((self.model , self.age , self.horse_power))
allc = [
        Car("mersedes" , 1999 , 127),
        Car("toyota" ,2021, 225),
        Car("bmw" ,2011, 216),
        Car("shkoda" ,1991, 86),
        ]
c1 = sorted(allc , key = lambda x: x.horse_power)
print(c1)

class Dog:
    def __init__(self , parod):
        self.parod = parod
    def can_i(self):
        print("i am", self.parod, "and i can bark")
d1 = Dog("Laika")
d1.can_i()
d2 = Dog("Shutterstock")
d2.can_i()

