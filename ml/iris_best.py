from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

csv = pd.read_csv('data/iris.csv')


irisData = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
irisLabel = csv['Name']

# grid-search params
params = [
    {"C": [1, 10, 100, 1000], "kernel": ['linear']},
    {"C": [1, 10, 100, 1000], "kernel": ['rbf'], "gamma": [0.001, 0.0001]},
]

trainData, testData, trainLabel, testLabel = train_test_split(irisData, irisLabel)
clf = GridSearchCV(svm.SVC(), params, n_jobs = -1, cv = 3, iid=True)
clf.fit(trainData, trainLabel)
print("machine=", clf.best_estimator_)

pred = clf.predict(testData)
score = metrics.accuracy_score(testLabel, pred)

# print(score)


# machine= SVC(C=1, cache_size=200, class_weight=None, coef0=0.0,
#   decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
#   kernel='linear', max_iter=-1, probability=False, random_state=None,
#   shrinking=True, tol=0.001, verbose=False)
# clff = svm.SVC(C=1000, cache_size=200, class_weight=None, coef0=0.0,
#   decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
#   max_iter=-1, probability=False, random_state=None, shrinking=True,
#   tol=0.001, verbose=False)
clff = svm.SVC(C=1, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
  kernel='linear', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
clff.fit(trainData, trainLabel)
# print("machine=", clff.best_estimator_)

pred = clff.predict(testData)
score = metrics.accuracy_score(testLabel, pred)

print(score)


# while True:
#     cmd = input("꽃받침의 길이, 꽃받침의 넓이, 꽃잎의 길이, 꽃잎의 넓이 >> ")
#     if not cmd: break
#     a, b, c, d = cmd.split(',')
#     p = clf.predict([[a, b, c, d]])
#     print("이름 = ", p[0])