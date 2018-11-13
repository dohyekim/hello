def write_file():
    with open("a.csv","w", encoding='utf8') as file:
        file.write("Name, S, A \n")
        file.write("김, M, 24 \n")
        file.write("John, M, 20 \n")


def add_file():
    with open("a.csv", "a") as file:
        file.write("Eileen, F, 24 \n")

def read_file():
    with open("a.csv","r", encoding='utf8') as file:
        for line in file:
            print(line)

write_file()

add_file()

read_file()

# 추가하고 싶을 때 "w" 대신 "a" 쓰면 됨.

# 한글을 추가하고 싶은 경우에는 encoding='utf8'를 꼭 추가해줘야 한다.