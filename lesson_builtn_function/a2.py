
with open("students.csv", "w", encoding='utf8') as file:
    file.write("이름, 성별, 나이, 성적\n")
    file.write("문별, 여, 27, 58\n")
    file.write("김용선, 여, 28, 77\n")
    file.write("안혜진, 여, 25, 82\n")
    file.write("정휘인, 여, 25, 79\n")
    file.write("김도혜, 여, 25, 92\n")
    file.write("문스타, 남, 24, 50\n")
    file.write("원미동, 여, 28, 39\n")
    file.write("문별이, 남, 29, 48\n")
    file.write("김정민, 여, 31, 72\n")
    file.write("전성호, 남, 35, 91\n")


with open("students.csv","r", encoding='utf8') as file:
    for line in file:
        print(line)


# 실행 필요
python a2.py