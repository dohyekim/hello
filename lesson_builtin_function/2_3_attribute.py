
# eval(code_str)과 같은 함수

class TestClass:
    name = "TEST"

    def static_method():
        print("STATIC!!")

    def get_name(self):
        print("QQQQQQQQQQQQQQ")
        return self.name

    def area(self,x,y):
        return x * y


test = TestClass()

print("1111>", test.get_name())

c = callable(test.get_name)
print("c==", c)   # c== True


class Child(TestClass):

    def get_name(self):
        t = super().get_name()  
        return "Child Name" + self.name
    
    def area(self, x, y):
        t = super().area()
        return t / 2

#getattr(instance, 'fn') : self가 있는 경우
#getattr(Class, 'fn') : static method인 경우

getattr(test, 'get_name')()  # attribute = property + method, get_name은 method니까 ()를 붙여 실행해야함.
getattr(TestClass, 'static_method')()  

class DA:

    def a(x,y):
        return x * y 

cmd = input("A>> ")
getattr(DA, cmd)()
