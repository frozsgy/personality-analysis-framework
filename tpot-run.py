# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import SCORERS
from tpot import TPOTClassifier

n = int(input("what's the word2vec dimension? "))

cols = ['class']
for i in range(n):
    cols.append('c'+str(i))

personalityType = input("which personality type? ")

limit = input("which algorithm do you want to use (knn/svm/nb/dt/rf)? ")

shuf = input("shuffled? (y/n): ")

fileName = #you need to write the name of the vector ground truth file here

data = pd.read_csv('resultvector-'+str(n)+'-25-7-'+s+'.csv',header=None)
data.columns = cols


knn = {

    'sklearn.neighbors.KNeighborsClassifier': {
        'n_neighbors': range(1, 101),
        'weights': ["uniform", "distance"],
        'p': [1, 2]
    }
}

svm = {

    'sklearn.svm.LinearSVC': {
        'penalty': ["l1", "l2"],
        'loss': ["hinge", "squared_hinge"],
        'dual': [True, False],
        'tol': [1e-5, 1e-4, 1e-3, 1e-2, 1e-1],
        'C': [1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1., 5., 10., 15., 20., 25., 45., 60., 75., 85., 100.]
    } 
}

dt = {

    'sklearn.tree.DecisionTreeClassifier': {
        'criterion': ["gini", "entropy"],
        'max_depth': range(1, 11),
        'min_samples_split': range(2, 21),
        'min_samples_leaf': range(1, 21)
    }
}


nb = {

    'sklearn.naive_bayes.GaussianNB': {
    },

    'sklearn.naive_bayes.MultinomialNB': {
        'alpha': [1e-3, 1e-2, 1e-1, 1., 5., 10., 15., 20., 25., 45., 60., 75., 85., 100.],
        'fit_prior': [True, False]
    }  
}

rf = {
        
    'sklearn.ensemble.RandomForestClassifier': {
        'n_estimators': [100],
        'criterion': ["gini", "entropy"],
        'max_features': np.arange(0.05, 1.01, 0.05),
        'min_samples_split': range(2, 21),
        'min_samples_leaf':  range(1, 21),
        'bootstrap': [True, False]
    }
}

if limit == 'knn':
    tpot_conf = knn
elif limit == 'svm':
    tpot_conf = svm
elif limit == 'dt':
    tpot_conf = dt
elif limit == 'nb':
    tpot_conf = nb
else:
    tpot_conf = rf

data_shuffle = data
if shuf == 'y':
    data_shuffle = data.iloc[np.random.permutation(len(data))]
data_features = data_shuffle.reset_index(drop=True)
data_class = data_features['class'].values


tpot = TPOTClassifier(generations=10,verbosity=2,cv=5,scoring="accuracy",template='Classifier',config_dict=tpot_conf)
tpot.fit(data_shuffle.drop('class',axis=1).values, data_class)
print("tpot score: ", tpot.score(data_shuffle.drop('class',axis=1).values, data_class))

filename = './tpot-pipeline-' + limit + '-' + str(n) + '-' + personalityType + '.py'
tpot.export(filename)

print("file exported to:", filename)


