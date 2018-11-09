#클래스에 아무것도 없으면 error

#x, y는 사각형에 있으니까 앞에 빼둠. 어차피 다 갖고 있음.

def to_int(s):
    if type(s) == str:              # #여기서 미리 x,y가 str으로 들어온다면  int로 바꿔주자 ==>함수로 만들어버리기
        return int(s)
    else:
        s

class Square:
    def __init__(self):
        print("\n @@@2 square created\n")


class Rec(Square):
    def 넓이(self,x,y):            #instance에서 받는 함수니까 self 필요
        return to_int(x) * to_int(y)            #혹시라도 str이 들어오면 int로 바꾸고 int로 들어오면 그냥 int로 쓰도록 이렇게 씀.


class Paral(Square):
    def 넓이(self,x,y):
        return to_int(x) * to_int(y)
 
#사각형의 종류
while(True):

    print() #input이 다음에 계속 나올 때 한 칸 떼기
    rect_type = input("사각형의 종류는? \n1.직사각형 \n2. 평행사변형 \n (quit:q)\n")
    if(rect_type == 'q'):
        break

    if rect_type == "1":
        rect = Rec()
        #rect.length(x, y) #여기서 x, y를 받아야 함.
        length = input("가로와 세로는? (usage: 가로, 세로)")
        x, y = length.split(',')
        result = rect.넓이(x,y)
        print("\n직사각형의 넓이는 {}이다".format(result))

    else:
        paral = Paral()
        #rect.넓이(x, y) #여기서 x, y를 받아야 함.
        under = input("밑변와 높이는? (usage: 밑변, 높이)")
        x, y = under.split(',')
        result = paral.넓이(x,y)
        print("\n평생사변형의 넓이는 {}이다".format(result))