import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics  

df = pd.read_csv("./data/mushroom.csv")
# print(df.shape)
# print(df.head)


allLabel = []
allData = [] # ->> [[s,t,t,d,...]]

for rowidx, row in df.iterrows():         # cf. enumerate
    allLabel.append(row.iloc[0]) 
# 문자 -> 숫자화       (데이터는 실수화(벡터화)해야 한다 )
    ords = []
    for c in row.iloc[1:]: # 1번째부터
        ords.append(ord(c)) #unicode의 값 (사실은 문자마다 이진수로 만드는 게 좋다. 데이터는 커지지만)
    allData.append(ords)

trainData, testData, trainLabel, testLabel = train_test_split(allData, allLabel)

clf = RandomForestClassifier(n_estimators=100, n_jobs=3, random_state=4096)       

clf.fit(trainData, trainLabel)

pred = clf.predict(testData)
score = metrics.accuracy_score(testLabel, pred)
report = metrics.classification_report(testLabel, pred)
