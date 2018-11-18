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


# full_name을 실행시키고 싶을 때
# print("FFFFFFFFF", test.full_name()) 
print("FFFFFFFFF", test.full_name)  #property니까 () 없는 것.

