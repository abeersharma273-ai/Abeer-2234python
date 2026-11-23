from abc import ABC, abstractmethod


class Base(ABC):
    def display(self, value):
        print("Value:", value)

    @abstractmethod
    def calculate(self, x):
        pass


class Square(Base):
    def calculate(self, x):
        return x * x


obj = Square()
obj.display(10)
result = obj.calculate(5)
obj.display(result)

try:
    b = Base()
except TypeError as e:
    print("Error:", e)
