
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

#제일 마지막에 while 걸기

while(True):

    cmd1 = input("사각형의 종류를 고르시오.  \n1. 직사각형  2. 평행사변형 \n")
    cmd = input("밑변, 높이>>> ")

    if cmd == "quit":
        break

    cmds = cmd.split(',')
    a = int(cmds[0])
    b = int(cmds[1])

    outmsg = "{}의 넓이는 {}입니다."

    if cmd1 == '1': 
        print(outmsg.format("직사각형",rec.multiply(a, b)),"\n")
    elif cmd1 == '2': 
        print(outmsg.format("평행사변형",paral.multiply(a, b),),"\n")






        
