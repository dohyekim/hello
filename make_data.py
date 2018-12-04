import random
import pymysql

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성무병별솔하라")
#insert into Student(name) values(?)
#executemany 쓰세요!!


def make_name():
    last_name = []
    last_name.append(random.choice(fam_names))

    name = random.sample(first_names, k = 2)

    full_name = ''.join(last_name + name)
    
    return full_name


def make_address():
    address = ["서울", "경기", "전북","전남","경북","경남","대전","충북","충남","대구","제주", "강원"]

    addr = random.choice(address)
    return addr

def make_phone():
    
    number = ['0','1','2','3','4','5','6','7','8','9'] * 4

    front_num = ''.join(random.sample(number, k= 4))
    back_num = ''.join(random.sample(number, k=4))
    entire_num = "{}-{}-{}".format("010",front_num,back_num)
    
    return entire_num


def make_day():

    year = random.randrange(1960,2006)

    month = random.randrange(1,12)

    
    even = [4,6,9,11]
    
    day = random.randrange(1,32)
    
    if month in even:
        day = random.randrange(1,31)
    elif month == 2:
        day = random.randrange(1,29)
    else:
        day = day

    birthday = "{}-{:02d}-{:02d}".format(year,month,day)

    return birthday

def make_email():
    a = list('abcdefghijklmnopqrstuvwxyz0123456789') * 7
    email_id = ''.join(random.sample(a, k=6))
    b = ['gmail.com','hanmail.net','naver.com','hotmail.com','nate.com']
    email_acc = ''.join(random.choice(b))
    account = "{}@{}".format(email_id, email_acc)

    return account


data = []
for i in range(1001):
    a = (make_address())
    data.append(a)

conn = pymysql.connect(
    host='localhost', 
    user='dooo', 
    password='1234!', 
    port=3307, 
    db='dooodb', 
    charset='utf8')

with conn:
    cur = conn.cursor()
    sql = "insert into Student(address) values(%s)"
    cur.executemany(sql, data)
    #print("AffectedRowCount is",cur.rowcount)??>..,,,,,,,.

    conn.commit()

# with conn:
#     cur = conn.cursor()
#     sql = "insert into Student(name, phone, birthday, email) values(%s,%s,%s,%s)"
#     cur.executemany(sql, data)
#     #print("AffectedRowCount is",cur.rowcount)??>..,,,,,,,.

#     conn.commit()


# a = ['abcdefghijklmnopqrstuvwxyz0123456789']

# print(type(a))  # <class 'list'>
# print(a) # ['abcdefghijklmnopqrstuvwxyz0123456789']

# b = list('abcdefghijklmnopqrstuvwxyz0123456789')
# print(type(b)) # <class 'list'>
# print(b) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

