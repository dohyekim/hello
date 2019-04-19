from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

# 최적의 값 찾기 ############

csv = pd.read_csv('data/iris.csv')

irisData = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
irisLabel = csv['Name']

params = [
    {"C": [1, 10, 100, 1000], "kernel": ['linear']},
    {"C": [1, 10, 100, 1000], "kernel": ['rbf'], "gamma": [0.001, 0.0001]},
]

trainData, testData, trainLabel, testLabel = train_test_split(irisData, irisLabel)
clf = GridSearchCV(svm.SVC(), params, n_jobs = -1, cv = 3, iid=True)
clf.fit(trainData, trainLabel)
print(clf.best_estimator_)

# 최적의 값 적용하기 ##########

clfBest = svm.SVC(C=1, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
  kernel='linear', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)


clfBest.fit(trainData, trainLabel)

pred = clfBest.predict(testData)
score = metrics.accuracy_score(testLabel, pred)

print(score)

