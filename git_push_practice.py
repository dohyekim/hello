import sys
import os
import datetime


def git_push():
    os.system("git add --all")
    os.system("git commit -am \"{}\"".format(input_msg))
    os.system("git push")

sa = sys.argv
now = datetime.datetime.now()


default_msg = "{} 강의".format(now.strftime('%Y-%m-%d')) # default_msg가 여기서 먼저 선언된 후에 input_msg = default_msg가 되어야 한다.
 

if len(sa) == 2:
    input_msg = sa[1]

if len(sa) <2:
    add_msg = input("Default? if yes : enter, no : message ")
    if add_msg == '':
        input_msg = default_msg
    else:
        add_msg = input_msg

git_push()