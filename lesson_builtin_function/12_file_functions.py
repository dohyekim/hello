
# 내장함수 open

# file = 데이터파일 의미

# source file은 우리가 만드는 file

file = open("filename", "w")   # mode: w:write, a:add, r:read ("file name, 모드") #파일을 연다

file.write("파일 내용") #쓴다 >>> 15byte썼다고 나ㅏ온다..

file.close()             #닫는다(lock 끝남), close()꼭 해야함. close하는 순간 저장됨.

with open("filename", "w") as file:           # "w"모드만 새로 만들 수 있음.
    
	file.write(".........")

with open("filename", "r") as file:    # 읽기 모드로 열었을 때, "as"는 별명을 붙일 때, "filename"을 file이라는 변수로 부르겠다.

	for line in file:   # for loop을 돌릴 수 있다는 건 list/tuple형식으로 왔다는 것. 
						#line은 변수 (필기에서의 t). 한 개의 line씩 들어온다.

		print(line)
