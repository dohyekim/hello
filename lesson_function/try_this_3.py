# 이름, 나이, 성별을 입력받아 "당신의 이름은 {}, 나이는 {}, 성별은 {}입니다." 출력하기

while (True):

    cmd = input("Usage: Your name, age, gender>>> ")

    if cmd == "quit":
        break
   
    if cmd == '':
        print("Name, age, gender is needed")
        continue


    if ',' not in cmd:
        print("Please write \",\" ")
        continue

    cmds = cmd.split(',')
    a = "Your name is {}, {} years old and you are {}."
    r = a.format(cmds[0], cmds[1], cmds[2])
    print(r)

    if len(cmds) != 3:
        print("Please write all the information")
        continue

    
    
