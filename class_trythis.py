
class Square:
    
    def __init__(self):
        self.name = Square
    
    def multiply(self, a, b):
        return a * b
        

class Paral(Square):
    def __init__(self):
        self.name = Paral

class Rec(Paral):
    def __init__(self):
        self.name = Rec

paral = Square()
print(paral.multiply(2,4))

square = Paral()
print(square.multiply(6,1))

rec = Square()
print(rec.multiply(9,2))

while (True):


    cmd = input("사각형의 종류, 밑변, 높이>>> ")
    if cmd == "quit":
        break
    
    cmds=cmd.split(',')

    a = int(cmds[1])
    b = int(cmds[2])
    kind = cmds[0]

    x = ["직사각형", "평행사변형"]
    if kind == x[0]:
        print(square.multiply(a,b))
    elif kind == x[1]:
        print(paral.multiply(a,b))
    elif kind != x:
        print("다시 써 주세요.")

