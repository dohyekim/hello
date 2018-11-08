
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


square = Paral()

rec = Square()



cmd1 = input("사각형의 종류를 고르시오. / |n 1. 직사각형 / 2. 평행사변형")

 c, d = int(1), int(2)
    
    if cmd1 == c or d:

        cmd = input("밑변, 높이>>> ")

    while(True):

        if cmd == "quit":
            break
    
        cmds = cmd.split(',')

        a = int(cmds[0])
        b = int(cmds[1])

        if cmd1 == c: 
            print(rec.multiply(a, b))
        if cmd1 == d:
            print(paral.multiply(a, b))


        
