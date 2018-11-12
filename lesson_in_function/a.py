class TestClass:
    name = "TEST"

    def static_method():
        print("STATIC")

    def get_name(self):
        print("QQQQQQQQQQQQQQ")
        return self.name
    
    # @property가 붙는 순간 얘는 함수가 아님. 대신 property(즉 변수)가 됨. 따라서 실행할 때 ()가 있으면 안 된다.
    @property
    def full_name(self):
        return self.name + "fffffff"
    

    def area(self, x, y):
        return x * y


# 부모의 logic을 대부분 쓰고 조금만 바꾸고 싶을 때
class Child(TestClass):
    def get_name(self):
        t = super().get_name()
        return "Child Name" + self.name
    
    def area(self, x, y):
        t = super().area(x, y)  ### t = super().areㅁ(x,y) 이렇게 하면 x*y는 부모 logic으로, 자식은 그 값을 /2하는 것만
        return t / 2

test = TestClass()
child = Child()

# full_name을 실행시키고 싶을 때
# print("FFFFFFFFF", test.full_name()) 
print("FFFFFFFFF", test.full_name)  #property니까 () 없는 것.

cmd = input("Input the function name>>> ")

getattr(test, cmd)()

#input에 get_name을 쓰면 get_name function이 실행됨

getattr(test, "get_name")()           #test.get_name과 같음. # ()은 함수의 실행을 의미
getattr(TestClass, "static_method")()

#property와  method를 합친 게 attribute. TestClass의 get_name이라는 함수를 가져온다.
#self가 있으면 instance
#self가 없으면 class를 쓴다.
#어떤 명령을 실행하고 싶을 때



#print("11111111111>>", test.get_name(), child.get_name())

#c = callable(test.get_name)

#print("CCCCCCCC>>", c) 


test.static_method() # error가 남. 왜냐하면 static_method는 self가 없는 static인데 instance를 줘서 오류
TestClass.static_method() #error안 남/

@staticmethod
def static_method():
    print("ST")

    # 이렇게 @staticmethod를 하면 instance로 부르든 class로 부르든 error 안 남
    # @staticmethod를 붙이면 

ord("aa")
ord("한")
bytearray("한글", UTF8)