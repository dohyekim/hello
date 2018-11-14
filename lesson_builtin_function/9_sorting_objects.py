class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):             # str화 해주세요.                   print(s)에서 s는 string
        return "{}:{}".format(self.name, self.score)

students = [
    Student("김일수", 10),
    Student("김삼수", 30),
    Student("김이수", 20)
]

def print_students():
    print("--------------------")
    for s in students:
        print(s)

print_students()


sort_students = sorted()
# 점수순으로 sorting하기

sort_students = sorted(students, key = lambda stu: stu.score)        #stu는 인자, 즉 def fn(stu): return stu.score의 의미. stu.score를 받아서 students에다 넣음.

print_students()

students.sort(key = lambda stu: stu.score)

print_students()

students.sort(key = lambda stu: stu.score, reverse=True)

print_students()

def sort_key(stu):

	return stu.score

students.sort(key = sort_key, reverse = True)

print_students()