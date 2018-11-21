import sqlite3
import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")
#insert into Student(name) values(?)
#executemany 쓰세요!!


def make_name():
    
    last_name = random.choice(fam_names)

    name = ''.join(random.sample(first_names, k = 2))

    return (last_name + name,) #tuple화 하기 : ,필수!
   
    #full_name_1 = str(full_name[0] + full_name[1] + full_name[2])




data = []
for i in range(0,3):
    data.append(make_name()


conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    sql = "insert into Student(name) values(?)"
    cur.executemany(sql, data)

    conn.commit()
