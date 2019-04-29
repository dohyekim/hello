from sklearn import svm, metrics    
import pandas as pd
from sklearn.externals import joblib
from pathlib import Path

def readCsv(file, maxcnt):
    labels = []
    images = []
    with open(file, "r") as f:
        for i, line in enumerate(f):
            if i >= maxcnt:
                break
            cols = line.split(",")
            labels.append(int(cols.pop(0)))
            images.append(list(map(lambda b: int(b) / 256, cols))) 
    return {"labels": labels, "images": images}


train = readCsv('./data/train.csv', 60000)  
test = readCsv('./data/t10k.csv', 10000)


# training ---------------------------
clf = svm.SVC(gamma='auto')
clf.fit(train['images'], train['labels'])

# test -------------------------
pred = clf.predict(test['images'])

score = metrics.accuracy_score(test['labels'], pred)
print("\n\nscore=", score)

print("-----------------------------------------")
report = metrics.classification_report(test['labels'], pred)
print(report)