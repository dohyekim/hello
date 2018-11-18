class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):             # 각각의 instance를 str화 해주세요.                   print(s)에서 s는 string
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

# students라고 하는 instance등을 str으로 만들어주세요.
# print(instance)하면 __str__의 과정을 겪는다.

print(students[0])


sort_students = sorted(students)
# 점수순으로 sorting하기

sort_students = sorted(students, key = lambda stu: stu.score)        
# stu는 인자, 즉 def fn(stu): return stu.score의 의미.
# stu.score를 받아서 students에다 넣음.
# sort_students = sorted(stu.score)가 되는 셈
# stu라는 인자를 가진 function을 받아서 stu.score를 return받는다. 

print_students()

students.sort(key = lambda stu: stu.score)

print_students()

students.sort(key = lambda stu: stu.score, reverse=True)

print_students()

def sort_key(stu):

	return stu.score

students.sort(key = sort_key, reverse = True)

print_students()