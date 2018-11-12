
def to_int(s):
    if type(s) == str:
        return int(s)
    else:
        return s

class Square:
    
    x, y = 0, 0

    def area(self, x, y):
        return to_int(x) * to_int(y)

class Rec(Square):
    def __init__(self):
        self.name = Rec

class Paral(Square):
    def __init__(self):
        self.name = Paral

square = Square()
rec = Rec()
paral = Paral()

while (True):

    cmd = input("사각형의 종류는? \n 1. 직사각형 2. 평행사변형 \n 3.quit = (quit) \n")
    
    if cmd == "3":
        break

    cmd_1 = input("밑변과 높이는? (Usage: x, y)>>>\n")


    cmds_1 = cmd_1.split(',')

    a = cmds_1[0]
    b = cmds_1[1]

    msg = "넓이는 {:d}입니다.\n"

    if cmd == '1':
        print(msg.format(rec.area(a, b)))

    if cmd == '2':
        print(msg.format(paral.area(a, b)))
