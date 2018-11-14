import sys

import mysys           # from mysys import clear_screen (이 방식을 더 선호)
mysys.clear_screen()   # clear_screen()


# __file__ #sys.argv[0] 의미
print("__file__ >>>>" __file__)
print(sys.argv, len(sys.argv))

def print_sys_vars():
    for i in [sys.version, sys.copyright, sys.path, sys.platform]:
        print("-------->",i)

print_sys_vars()


# 파일 내용을 보여주는 프로그램

sa = sys.argv
if len(sa) < 2:
    sys.exit()
with open (sa[1], "r", encoding = 'utf=8') as file:
    for line in file:
        print(line.strip())
