import sqlite3

class Student:

    def __init__(self):
        name, gender, age, score, address = line.split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)
        self.address = address

    gen = ''

    def m_gender(self):
        if self.gender == "남":
            self.gen = "M"
        elif self.gender == "여":
            self.gen = "F"
    
    addr = ''

    def m_address(self):
        a = self.address.split(' ')
        self.addr = " ".join(a[1:3])

    grade = ''

    def make_grade(self):
        if self.score // 10 >= 9:
            self.grade = "A"
        elif self.score // 10 == 8:
            self.grade = "B"
        elif self.score // 10 == 7:
            self.grade = "C"
        elif self.score // 10 == 6:
            self.grade = "D"
        elif self.score // 10 < 6:
            self.grade = "F"

    def __str__(self):
        return "{}**\t{}\t{}0대\t{}\t{}".format(self.name[0], self.gen, self.age[0], self.grade, self.addr)        

l = self.name, self.gender, self.age, self.score, self.address

students = []
with open("students.csv", "r", encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0:
            continue
        students.append(Student())

def print_students():
    for s in students:
        print(s)

filter1 = filter(lambda stu: stu.make_grade(), students)
list(filter1)
  
filter2 = filter(lambda stu: stu.m_gender(), students)
list(filter2)

filter3 = filter(lambda stu: stu.m_address(), students)
list(filter3)

print_students()

# import sqlite3


# params = []
# with open('students.csv', 'r', encoding='utf-8') as file:
#     for i, line in enumerate(file):
#         if i == 0: continue
#         stu = Student(line)
#         t = stu.make_params()
#         # print(type(t), list(t))
#         params.append(t)

# # print(params)

# conn = sqlite3.connect("exam.db")

# def insert_data():
#     with conn:
#         cur = conn.cursor()
#         sql = "insert into Student(name, gender, age, grade, addr) values(?,?,?,?,?)"
#         cur.executemany(sql, params)

#         conn.commit()

# def select_data():
#    with conn:
#         cur = conn.cursor()
#         # sql = "select id, name, gender, age, grade, addr from Student order by grade"
#         sql = """select id, name, gender, age, grade, addr
#                    from Student order by substr(grade,1,1), grade desc"""
#         # print(sql)
#         cur.execute(sql)
#         rows = cur.fetchall();
#         for row in rows:
#             print(row)

# insert_data()
# select_data()