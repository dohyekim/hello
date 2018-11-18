class TestClass:
    name = "TEST"

    @staticmethod
    def static_method():
        print("STATIC")

    # 이렇게 @staticmethod를 하면 instance로 부르든 class로 부르든 error 안 남


test = TestClass()

test.static_method()
TestClass.static_method()

# 원래는 test.static_method() --> error. test : insntance, static_method() : static method
# but with @staticmethod, test.static_method --> Okay

    