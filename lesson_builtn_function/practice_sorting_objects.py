class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):             # str화 해주세요.                   print(s)에서 s는 string
        return "{}:{}".format(self.name, self.score)

#instance 만들기
students = [
    Student("김일수", 10),
    Student("김삼수", 30),
    Student("김이수", 20)
]

print(students[0])       #>>김일수:10

#만일 def __str__이 없다면 #>>><__main__.Student object at 0x03228BB0> 즉 주소가 나옴

def print_students():
    print("--------------------")
    for s in students:
        print(s)


students.sort(key = lambda stu: stu.score)
print_students()

ss = sorted(students, key = lambda stu: stu.score)
print_students()
