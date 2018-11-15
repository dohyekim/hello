import sys
import os
import datetime


def git_push(msg):
    os.system("git add --all")
    os.system("git commit -am \"{}\"".format(msg))
    os.system("git push")

sa = sys.argv
now = datetime.datetime.now()


default_msg = "{} 강의".format(now.strftime('%Y-%m-%d')) # default_msg가 여기서 먼저 선언된 후에 input_msg = default_msg가 되어야 한다.
input_msg = default_msg                 # input_msg = default_msg가 없으면 input_msg가 defined되지 않았다고 뜬다.
 

if len(sa) == 2:
    input_msg = sa[1]

if len(sa) <2:
    add_msg = input("Default? if yes : enter, no : message ")
    if add_msg == '':
        input_msg = default_msg
    else:
        input_msg = add_msg             # add_msg를 input_msg에 담는다. #add_msg = input_msg  는 잘못된 코드

git_push(input_msg)

# 주석은 간단하지 않은 경우에는 상단에 적는다.