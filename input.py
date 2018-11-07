


cmd = input("Input(usage: 이름, 나이, 성별)>> ")
print(cmd) # cmd = 'a, b, c'

#1. 값의 존재여부 체크
if cmd == ' ':
    print("답을 채워주세요.")
    exit()

# if cmd.(isspace):
#   print("답을 채워주세요.")

# if cmd.find(',') == -1: 

errormsg = "다시 해주세요."
#2. ,가 있는지 없는지

if ',' not in cmd:
    print(errormsg)
    exit()

cmds = cmd.split(',') # cmds = ['a', 'b', 'c'] 즉 list로 쪼갬


#3. 값이 3개인지
if len(cmds) != 3:
    print("3가지를 모두 입력해주세요.")
    exit()

outmsg = "제 이름은 {}, 나이는 {}, 성별은 {}입니다."

print(outmsg.format(cmds[0],cmds[1],cmds[2]))
