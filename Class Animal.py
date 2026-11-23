from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("Human walks on two legs")


class Dog(Animal):
    def move(self):
        print("Dog runs on four legs")


animals = [Human(), Dog()]

for a in animals:
    a.move()

try:
    x = Animal()
except TypeError as e:
    print("Error:", e)
