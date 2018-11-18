class TestClass:
    name = "TEST"

    def get_name(self):
        print("QQQQQQQQQQQQQQ")
        return self.name


test = Testclass()
print("1111>", test.get_name())

c = callable(test.get_name)
print("c==", c)
