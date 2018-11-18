class TestClass:
    name = "TEST"

    def get_name(self):
        print("QQQQQQQQQQQQQQ")
        return self.name

    def area(self,x,y):
        return x * y


test = Testclass()

print("1111>", test.get_name())

c = callable(test.get_name)
print("c==", c)

class Child(TestClass):
        def get_name(self):
        super().get_name()
        return self.name

child = Child()


# 부모의 logic을 대부분 쓰고 조금만 바꾸고 싶을 때
class Child(TestClass):

    def get_name(self):
        t = super().get_name()  # print("QQQQQQQQQQQQQQ")된 후에 밑의 return값을 수행한다.
        return "Child Name" + self.name
    
    def area(self, x, y):
        t = super().area()
        return t / 2

