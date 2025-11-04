from oopsClass import Calculator


class ChildClass(Calculator):
    num1 = 200

    def __init__(self):
        Calculator.__init__(self, 12, 22)
    def getCompleteValue(self):
        return self.num1 + self.num + self.summation()
    def getParentMethod(self):
        Calculator.getData(self)

obj = ChildClass()
print(obj.getCompleteValue())
print(obj.getParentMethod())