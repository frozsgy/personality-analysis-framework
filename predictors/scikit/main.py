from sklearn import svm
from sklearn import datasets
from numpy import array
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import NearestCentroid
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix

samples = 30
test = 0

with open("resultvector-cut.csv") as f:
    vectorFile = f.readlines()
vectorFile = [x.strip() for x in vectorFile]
vectorFile = vectorFile[1:]

vectorString = []
for eachLine in vectorFile:
    vectorString.append(eachLine.split(","))
vector = []
for eachVector in vectorString:
    temp = []
    for eachNumber in eachVector:
        temp.append(float(eachNumber))
    vector.append(temp)



with open("GT2.txt") as f:
    truthFile = f.readlines()
truthFile = [x.strip() for x in truthFile]

truths = []
for i in range(5):
    temp = []
    for eachLine in truthFile:
        temp.append(int(eachLine.split(" ")[i]))
    truths.append(temp)


def train(method):
    scores = []
    for i in range(5):

        X = array(vector[:samples])
        y = array(truths[i])

        clf = method

        clf.fit(X, y)
        crossValScores = cross_val_score(clf, X, y, cv=2)
        crossValScore = crossValScores.mean()

        prediction = clf.predict(vector[:samples])
        """print('----------------------')
        print(i)
        print('----------------------')"""
        index = 0
        #for eachLabel in truths[i]:
        y_pred = cross_val_predict(clf, X, y, cv=2) 

        conf_mat = confusion_matrix(y, y_pred)
        prediction_new = 0.0
        index1 = 0
        for eachLabel in conf_mat:
            index2 = 0
            for eachPrediction in eachLabel:
                prediction_new += eachPrediction * float( 3.0 - abs(index1-index2) ) / 3.0
                index2 += 1
            index1 += 1
        #print(prediction_new/30)
        real = truths[i]
        label = list("OCEAN")
        scores.append([label[i], prediction_new/samples, accuracy_score(real, prediction), str(round(crossValScore,2)) + " (+/- " + str(round(crossValScores.std() * 2, 2)) + ")" ])

    return scores

print("Training data with different methods...")

scores = {}
classifiers = [RandomForestClassifier(n_estimators=10), NearestCentroid(), svm.SVC(), svm.LinearSVC(max_iter=15000)]
for classifier in classifiers:
    scores[classifier] = train(classifier)

print("Training complete")

l = ["Type", "Prediction", "Accuracy Score", "SD"]

from tabulate import tabulate
for eachScore in scores:
    print(eachScore)
    print(tabulate(scores[eachScore], headers=l))
    #print(scores[eachScore])
    print('\n')

t_inv = list(zip(*truths))
guess = [[-0.352269157,0.07927927,0.526288862,0.040001991,0.093700687,-0.129675139,0.37161941,0.168640847,-0.031083506,-0.18462781,0.472268887,0.004425106,0.101193233,0.216093556,-0.04838439,0.315387216,0.115871034,-0.495221181,-0.052879347,-0.432659209,-0.401077351,0.199863161,0.406283452,0.051968577,0.248381509,0.171477028,0.259955049,-0.337053881,-0.120273434,0.605412169,-0.331642057,0.025143943,-0.107368211,-0.169768232,0.154180114,-0.15068825,-0.365644523,-0.405429543,0.25,0.25,0.75,0.75,0,0.75,0,0.25,0.25,0.75,0.25,0.25,0.75,1,0,0.75,0,0.75,0.25,0.75]]

print("Predictions used trained data")

################## 
print("-"*80)
print("RandomForestClassifier PREDICTION")
print("Expected : [3, 3, 3, 2, 2]")
X, y = array(vector), array(t_inv)
#knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn = RandomForestClassifier(n_estimators=10)
knn.fit(X, y)
print("Result   : " + str(knn.predict(guess).tolist()[0]))

################## 
print("-"*80)
print("SVC PREDICTION")
print("Expected : [3, 3, 3, 2, 2]")
r = []

for i in range(5):
    X, y = array(vector), array([x[i] for x in t_inv])
    knn = svm.SVC()
    knn.fit(X, y)
    r.append(knn.predict(guess)[0])
print("Result   : " + str(r))


##################
print("-"*80)
print("NearestCentroid PREDICTION")
print("Expected : [3, 3, 3, 2, 2]")
r = []

for i in range(5):
    X, y = array(vector), array([x[i] for x in t_inv])
    knn = NearestCentroid()
    knn.fit(X, y)
    r.append(knn.predict(guess)[0])
print("Result   : " + str(r))

################## 
r = []
print("-"*80)
print("LinearSVC PREDICTION")
print("Expected : [3, 3, 3, 2, 2]")

for i in range(5):
    X, y = array(vector), array([x[i] for x in t_inv])
    knn = svm.LinearSVC(max_iter=15000)
    knn.fit(X, y)
    r.append(knn.predict(guess)[0])
print("Result   : " + str(r))


