import datetime

now = datetime.datetime.now()
# datetime이라는 package에 있는 datetime module
now.year, now.month, now.day, now.hour, now.minute, now.second

now.strftime('%Y-%m-%d %H:%M:%S') #string format time

now.strftime('%Y{} %m{} %d{} %H{} %M{}'.format(*"년월일시분")) # *를 붙이면 string을 한 글자 단위로 쪼개서 list로 만들어준다. 

now + datetime.timedelta(weeks=1) # days, hours, minutes, seconds

# timedelta(단위) now 지금 시간에다가 + weeks=1을 더한 시간이 나옴.

now.replace(year = (now.year + 1))
