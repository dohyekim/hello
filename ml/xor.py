from sklearn import svm, metrics
import pandas as pd
#(Support Vector Machine)

# training set
xor_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

df = pd.DataFrame(xor_data) 

# print("shape>> \n", df.shape, "\n") # (4,3)
# print("head>> \n", df.head, "\n")
# print("columns>> \n", df.columns, "\n")
# print("columns>> \n", list(df.columns), "\n")
# print("index>> \n", len(df.index), "\n")
# print(df.loc[:, 0:1])


clf = svm.SVC(gamma='auto')   # Support Vector Classification
clf.fit(df.loc[:, 0:1], df.loc[:, 2]) # 실행시키면 model이 clf에 담겨짐 

# testset
testset = [[0, 1], [1, 0], [1, 1], [2, -1]]
pred = clf.predict(testset)
print("pred>>>>>", pred)

# () 안에다가는 정답을 줌
score = metrics.accuracy_score([1,1,0, 1], pred)
print("score>>> ", score)

while True:
    cmd = input("put x, y >> ")
    if not cmd:
        break
    x,y = cmd.split(' ')
    p = clf.predict([[int(x), int(y)]])
    print('참' if p[0] == 0 else '거짓')



xandy_data = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1],
    [2, 0, 0],
    [2, 1, 0],
    [2, 2, 1],
    [2, 3, 0],
    [3, 0, 0],
    [3, 1, 0],
    [3, 2, 0],
    [3, 3, 1]
]

df = pd.DataFrame(xandy_data) 


mdl = svm.SVC(gamma='auto')   # Support Vector Classification
mdl.fit(df.loc[:, 0:1],df.loc[:, 2])

testset2 = [[0,0], [1,1], [1,0], [1,3]]
p = mdl.predict(testset2)
print(" I think >>> ", p)

acc = metrics.accuracy_score([1,1,0,0], p)
print(" Score is >>> ", acc)

while True:
    cmd2 = input("put x, y >> ")
    if not cmd2:
        break
    a,b = cmd2.split(' ')
    p = mdl.predict([[int(a), int(b)]])
    print('참' if p[0] == 1 else '거짓')