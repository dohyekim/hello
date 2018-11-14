#students.csv 파일에 10명의 학생정보(이름,성별,나이,성적) 있습니다.
#(홍길동,남,23,80)
#이 파일을 읽어 성적순으로 출력하되,
#이름은 홍** 형태로, 성적은 학점으로 표현, 총점과 평균을 구하시오.
#그리고 상위 50%의 학생은 별도로 이름과 성적만 출력하시오.
g_grades = ["A","b","c","d","f"]
g_grades.reverse()

class Student:
    def __init__(self, line):
        name, gender, age, score = line.strip().split(",")
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)
    
    def make_grade(self):
        if self.score == 100:
            self.grade = "A"
        else:
            self.grade = g_grades[self.score // 10 - 5] 

    def __str__(self):             # str화 해주세요.                   print(s)에서 s는 string
        return "{}\t{}\t{}\t{}".format(self.name, self.gender, self.age, self.grade )

students = []
    with open("students.csv","r", encoding='utf8') as file:
        for i, line in enumerate(file):
            if i == 0:
                continue
            students.append( Student(line) )

students.sort(key = lambda stu:stu.score, reverse = True)
m = map(lambda x : x)

map1 = map(lambda x: x * 2, int_numbers)
print(list(map1))             # [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10] 
