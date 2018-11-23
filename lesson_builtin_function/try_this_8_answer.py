from functools import reduce




g_grades = ["A", "B", "C", "D", "F"]
g_grades.reverse()

class Student:
    grade = ''
    def __init__(self, line):
        name, gender, age, score = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)
    
    # student라는 객체(instnace)가 {}에 들어갈 수 있는 str이 될 수 있게 만들어주는 것.
    def __str__(self):
        return "{}**\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.grade)

    def make_grade(self):
        if self.score == 100:
            self.grade = "A+"
        else:
            self.grade = g_grades[ self.score // 10 - 5]

students = []
with open("students12.csv", "r", encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0: continue         # 이름,성별,나이,점수 없애려고
        students.append( Student(line) )  # Student(line)이라고 만든 instance를 30번째 line에서 만든 students list에 쏙 들어가는 것.

students.sort(key = lambda stu: stu.score, reverse = True)

m = map(lambda stu: stu.make_grade(), students)           # map은 값을 가지고 있는 게 아니라 주소만 알고 있음. 
print(list(m))                                                # map의 값을 출력

print("이름\t성별\t나이\t학점")
print("----\t----\t----\t----")

for s in students:
    print(s)


score_sum = reduce(lambda x, y: (x if type(x) == int else x.score) + y.score, students)   # sigma i=1~4일 때 lst
print("총점 >>> ", score_sum) 


score_mean = score_sum / len(students)
print(score_sum, score_mean)

for s in students:
    if s.score >= score_mean:
        print(s.name, s.score)

