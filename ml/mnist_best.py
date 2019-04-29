from sklearn.model_selection import GridSearchCV

# grid-search params
params = [
    {"C": [1, 10, 100, 1000], "kernel": ['linear']},
    {"C": [1, 10, 100, 1000], "kernel": ['rbf'], "gamma": [0.001, 0.0001]},
]
clf = GridSearchCV(svm.SVC(), params, n_jobs = -1, cv = 3, iid=True)

# clf = svm.SVC(gamma='auto')   # old training
clf.fit(train['images'], train['labels'])


print("machine=", clf.best_estimator_)
