import sys
import os

msg= input("메시지를 입력하세요 >>>")


def git_push():
    os.system("git add --all")
    os.system("git commit -am \"{}\"".format(msg))
    os.system("git push")

git_push()
