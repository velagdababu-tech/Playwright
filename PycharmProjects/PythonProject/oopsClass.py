#self keyword is mandatory for calling variables names into method
#instance and class variables have whole different purpose
#constructor name should be _init_
#new keyword is not required when we create object

class Calculator:
    num = 100

    #def constructor
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am call automatically")

    def getData(self):
        print("I am now Executing the method in the class")

    def summation(self):
        return self.firstNumber + self.secondNumber + self.num

obj = Calculator(2, 6)
obj.getData()
print(obj.summation())

obj1 = Calculator(4, 7)
obj1.getData()
print(obj1.summation())