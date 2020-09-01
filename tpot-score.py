# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import SCORERS
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from tpot import TPOTClassifier

n = int(input("what's the dimension: "))

print("shuffled? (y/n):")
shuf = input()

fileName = #you need to write the name of the vector ground truth file here
data = pd.read_csv(fileName,header=None)

cols = ['class']
for i in range(n):
    cols.append('c'+str(i))

data.columns = cols

#you need to write the output in the file that tpot-run.py exports here
pipeline = RandomForestClassifier(bootstrap=False, criterion="gini", max_features=0.7500000000000001, min_samples_leaf=7, min_samples_split=2, n_estimators=100) #this is a sample pipeline


shuffled = data
if shuf == 'y':
    shuffled = data.iloc[np.random.permutation(len(data))]

a = 0
p = 0
r = 0
f = 0

#cv 
cvf = 5
datasize = len(data)
cnt = datasize//cvf

for fold in range(cvf):
    test = shuffled.iloc[(fold*cnt):((fold*cnt)+cnt)]
    testing = test.reset_index(drop=True)
    test_class = testing['class'].values
    pre = shuffled.iloc[0:(fold*cnt)]
    post = shuffled.iloc[((fold*cnt)+cnt):datasize]
    train = pd.concat([pre,post],axis=0)
    training = train.reset_index(drop=True)
    train_class = training['class'].values
    pipeline.fit(train.drop('class',axis=1).values, train_class)
    aac = SCORERS['accuracy'](pipeline, test.drop('class',axis=1).values, test_class)
    print("fold ", fold , " score: ", aac)
    a += aac

print("overall accuracy:", a/cvf)


