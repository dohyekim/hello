from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split

csv = pd.read_csv('data/iris.csv')

irisData = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
irisLabel = csv['Name']

trainData, testData, trainLabel, testLabel = train_test_split(irisData, irisLabel)
clf = svm.SVC(gamma='auto')   # Support Vector Classification
clf.fit(trainData, trainLabel)

pred = clf.predict(testData)
score = metrics.accuracy_score(testLabel, pred)

# print(score)

while True:
    cmd = input("꽃받침의 길이, 꽃받침의 넓이, 꽃잎의 길이, 꽃잎의 넓이 >> ")
    if not cmd: break
    a, b, c, d = cmd.split(',')
    p = clf.predict([[a, b, c, d]])
    print("이름 = ", p[0])