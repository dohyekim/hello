# a = list("camus")
# print(a[0:])

# author = "Camus"
# print(author[0])
# print(author[1])
# print(author[2])
# print(author[3])
# print(author[4])

my = {}
my = {"키":"156",
"좋아하는 색깔":"블루",
"좋아하는 작가":"책을 안 읽어서 딱히 없음"}


while True:

    cmd = input("궁금한 것을 물어보세요 >> 1) 키 2) 좋아하는 색깔 3) 좋아하는 작가 q:quit \n")

    if cmd == 'q':
        print("안녕")
        break

    if cmd == '1':
        print(my["키"], "\n")
    
    elif cmd == '2':
        print(my["좋아하는 색깔"], "\n")
    
    elif cmd == '3':
        print(my["좋아하는 작가"], "\n")
    
    else:
        print("제대로 입력하세요.", "\n")


