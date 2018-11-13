class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return "{}:{}".format(self.name, self.score)

students = [
    Student("김일수", 10),
    Student("김삼수", 30),
    Student("김이수", 20)
]


sort_students = sorted(students, key = lambda stu: stu.score)

print_students()

students.sort(key = lambda stu: stu.score)

print_students()

students.sort(key = lambda stu: stu.score, reverse=True)

print_students()

def sort_key(stu):

	return stu.score

students.sort(key = sort_key, reverse = True)

print_students()