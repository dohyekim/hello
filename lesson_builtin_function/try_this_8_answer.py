from functools import reduce

from Student import Student

students = []
with open("students.csv", "r", encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0: continue         # 이름,성별,나이,점수 없애려고
        students.append( Student(line) )  # Student(line)이라고 만든 instance를 30번째 line에서 만든 students list에 쏙 들어가는 것.

students.sort(key = lambda stu: stu.score, reverse = True)

m = map(lambda stu: stu.make_grade(), students)           # map은 값을 가지고 있는 게 아니라 주소만 알고 있음. 
list(m)                                                # map의 값을 출력

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

