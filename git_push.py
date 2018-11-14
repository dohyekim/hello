import sys
import os
import datetime

sa = sys.argv # [0] 실행파일,  [1] 메시지 

now = datetime.datetime.now()
default_msg = "{} - 강의".format(now.strftime('%Y-%m-%d'))
commit_msg = default_msg
has_msg = len(sa) >= 2

if has_msg:      # len(sa) >= 2라면
    commit_msg = sa[1]  # sa[1]에 적은 걸 commit_msg로 받는다.

if has_msg == False:   # else:
    input_msg =input("Default Message?? (Yes:Enter or input message)")
    if input_msg != '':
        commit_msg = input_msg

def git_push():

    os.system("git add --all")
    os.system("git commit -am \"{}\"".format(commit_msg))
    os.system("git push")

git_push()

