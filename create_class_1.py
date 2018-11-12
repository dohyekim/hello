class Dog:
    
    def __init__(self):
        self.name = "dog"
        print("안녕안녕")
    # 숨겨둔 함수 __
    def __speak(self):
        print("왈왈", self.name)

    def wag(self):
        print("살랑살랑")

    def __del__(self):
        print("안녕")


class Puppy(Dog):
    def __init__(self):
        self.name = "강아지"
        print("안녕", self.name)

    def speak(self):
        print(self.name, "는 멍멍하고 짖는다")

    def sing(self):
        print(self.name, "는 노래도 한다")
    
    def __del__(self):
        print("안녕")

d = Dog()
d.wag()

p = Puppy()
p.wag
