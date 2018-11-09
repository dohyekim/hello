#클래스에 아무것도 없으면 error


#x, y는 사각형에 있으니까 앞에 빼둠. 어차피 다 갖고 있음.

class Casting:       #(self)없음! instance 만들 필요 ㅇ없음 #Class (집) 지어준 셈
    def to_int(s):
        if type(s) == str:              # #여기서 미리 x,y가 str으로 들어온다면  int로 바꿔주자 ==>함수로 만들어버리기
            return int(s.strip())           #5,   3 으로 주어지는 경우 3 앞의 space를 지우자
        else:
            return s


class Square:
    x, y = 0, 0                 #초기화
   
    name = "사각형" #msg에서 다른 부분이 "직사각형"이냐 "평행사변형"이냐만 다르니까 함수로 따로 빼기 위해서 여기에서 변수 만듦
    msg = "가로와 세로는?"   #가로와 세로, 밑변과 높이 "입력하라는 것만" 다르니까 가로,세로와 밑변,높이를 변수로 두고 하면 된다.
   
    def __init__(self):
        print("\n @@@2 square created\n")
    
   # def set_msg(self, msg):         # msg는 평사랑 직사 ㅈ다르니까
    #    self.msg = msg               # 방금 받은 msg self에는 msg라는 스트링을 넣겠다. 

    def input_data(self):               # 가로,세로 input은 모든 자식들이 받으니까 아예 부모Class에 놓는다.
        datum = input(self.msg)             #datum은 둘 때 만들어지는 local변수, input으로 받는 msg를 datum에 저장한다는 의미
        data = datum.split(',')
                                  #data는 두 가지 값이 들어올 것 ['5', '3'] ->얘를 여기서 int로 만들어버리자             
        x = Casting.to_int(data[0])        #x, y는 가로/밑변과 세로/높이 변수
        if len(data) <2:
            y = x
        else:
            y = Casting.to_int(data[1])
        self.__new_넓이(x, y)                 # new_넓이는 밖에서 부르지 못하도록 해야 함 (input이 들어와야만 돌아가니까) -> encapsulation
        # self.넓이()


    def __new_넓이(self, x, y):
        r = x * y
        print("{}의 넓이는 {}이다.".foramt(self.name, r))    #self.name에 직사각형이나 평행사변형이 들어갈 것. 왜냐하면 instance를 만들 때 이 새넓이 함수도 갖고 들어갈 것. 그럼 그 때의 self.name은 그 insntance 내의 self.name이 될 것
        

class Rec(Square):
    name = "직사각형"

class Paral(Square):
    name = "평행사변형"
    msg = "밑변과 높이는?"

class 정사각형(Square):
    name = "정사각형"
    msg = "한 변의 길이는?"

all_rects =  [Square(), Rec(), Paral(), 정사각형()]  # 나중에 여기다가 정사각형 추가하기 # all_rects = [직사각형(), 평행사변형()]라고 두면, #square = Square() 없앤 것
#0을 쓰면 자동으로 square가 뜨도록 Square()를 맨 앞에 추가

first_msg = '사각형의 종류는?\n'
for i, r in enumerate(all_rects):                   #enumerate: index와 value를 함께받을수있다.
    if i == 0:
        continue
    first_msg += "{d}) {}\n".format(i+1, r.name)       #i는 0부터 시작    # 1)직사각형  얘를 만들려는 것 

first_msg += "(quit:q)\n"
#사각형의 종류
while(True):

    print("--------------")
    rect_type = input(first_msg)
    
    
    if(rect_type == 'q'):
        break

    #이제 if를 지워보자.

    rect_index = Casting.to_int(rect_type)     ## 1. 직사각형을 숫자로 바꾼 후(1)에 -1 하면 0이 됨. all_rects에 [0]이 되면 직사각형, 2 -1하면 1 all_rects[1]이 되면 평행사변형

    if rect_index >= len(all_rects):              #나중에 5같은 게 들어왔을 때를 방지
        rect_index = 0

    rect = all_rects[rect_index]                              
    rect.input_data()            # Square에 있는 input_data를 물려받았기 때문에 rect.input_data()라고 쓸 수 있다.

#split에서는 error 안 남. 3이 주어지면 3만 남을 것이기 때문에