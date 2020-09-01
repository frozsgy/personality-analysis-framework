import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import SCORERS
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from tpot import TPOTClassifier


class teapot:

    __features = 20
    __dimensions = 75
    __top_words = 25
    __window_size = 7
    __personality_type = 'E'
    __shuffled = True
    __generations = 10
    __verbosity = 2
    __folds = 5
    __save_to_file = False

    __columns = ['class']
    __original_data = None
    __data = None
    __data_features = None
    __data_class = None
    __predictors = dict()

    def __init__(self, dimensions, personality_type, window_size = 7, top_words = 25, shuffled = True, generations = 10, verbosity = 2, folds = 5, save_to_file = False):
        self.__dimensions = dimensions
        self.__personality_type = personality_type
        self.__window_size = window_size
        self.__top_words = top_words
        self.__shuffled = shuffled
        self.__generations = generations
        self.__verbosity = verbosity
        self.__folds = folds
        self.__save_to_file = save_to_file
        self.__columns += ['c' + str(i)
                           for i in range(self.__features + self.__dimensions)]

        source_file = 'resultvector-{}-{}-{}-{}.csv'.format(self.__dimensions, self.__top_words, self.__window_size, self.__personality_type)
        self.__original_data = pd.read_csv(source_file, header=None)
        self.__original_data.columns = self.__columns
        self.__load_predictors()
        self.__shuffle_data()
        self.__load_features()

    def __load_predictors(self):

        self.__predictors['knn'] = {

            'sklearn.neighbors.KNeighborsClassifier': {
                'n_neighbors': range(1, 101),
                'weights': ["uniform", "distance"],
                'p': [1, 2]
            }
        }

        self.__predictors['svm'] = {

            'sklearn.svm.LinearSVC': {
                'penalty': ["l1", "l2"],
                'loss': ["hinge", "squared_hinge"],
                'dual': [True, False],
                'tol': [1e-5, 1e-4, 1e-3, 1e-2, 1e-1],
                'C': [1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1., 5., 10., 15., 20., 25., 45., 60., 75., 85., 100.]
            }
        }

        self.__predictors['dt'] = {

            'sklearn.tree.DecisionTreeClassifier': {
                'criterion': ["gini", "entropy"],
                'max_depth': range(1, 11),
                'min_samples_split': range(2, 21),
                'min_samples_leaf': range(1, 21)
            }
        }

        self.__predictors['nb'] = {

            'sklearn.naive_bayes.GaussianNB': {
            },

            'sklearn.naive_bayes.MultinomialNB': {
                'alpha': [1e-3, 1e-2, 1e-1, 1., 5., 10., 15., 20., 25., 45., 60., 75., 85., 100.],
                'fit_prior': [True, False]
            }
        }

        self.__predictors['rf'] = {

            'sklearn.ensemble.RandomForestClassifier': {
                'n_estimators': [100],
                'criterion': ["gini", "entropy"],
                'max_features': np.arange(0.05, 1.01, 0.05),
                'min_samples_split': range(2, 21),
                'min_samples_leaf':  range(1, 21),
                'bootstrap': [True, False]
            }
        }

    def __shuffle_data(self):
        if self.__shuffled is True:
            self.__data = self.__original_data.iloc[np.random.permutation(
                len(self.__original_data))]
        else:
            self.__data = self.__original_data

    def __load_features(self):
        self.__data_features = self.__data.reset_index(drop=True)
        self.__data_class = self.__data_features['class'].values

    def get_pipeline(self, predictor):
        tpot = TPOTClassifier(generations=self.__generations, verbosity=self.__verbosity, cv=self.__folds, scoring="accuracy", template='Classifier', config_dict=self.__predictors[predictor])
        tpot.fit(self.__data.drop('class', axis=1).values, self.__data_class)
        print("TPOT Score: ", tpot.score(self.__data.drop('class', axis=1).values, self.__data_class))

        if self.__save_to_file is True:
            filename = './tpot-pipeline-{}-{}-{}.py'.format(predictor, self.__features + self.__dimensions, self.__personality_type)
            tpot.export(filename)
            print("Pipeline exported to: {}".format(filename))
            return

        tpot_result = tpot.export()

        pipeline = filter(lambda i: "exported_pipeline = " in i, tpot_result.splitlines())
        pipeline = list(pipeline)[0].split("exported_pipeline = ")[1]

        print("\nPipeline: ", pipeline)

        return pipeline

    def score(self, predictor):
        result = []
        pipeline = eval(self.get_pipeline(predictor))

        datasize = len(self.__data)
        cnt = datasize // self.__folds

        for fold in range(self.__folds):
            test = self.__data.iloc[fold * cnt:fold * cnt + cnt]
            testing = test.reset_index(drop=True)
            test_class = testing['class'].values
            pre = self.__data.iloc[0:fold * cnt]
            post = self.__data.iloc[fold * cnt + cnt:datasize]
            train = pd.concat([pre, post], axis=0)
            training = train.reset_index(drop=True)
            train_class = training['class'].values
            pipeline.fit(train.drop('class', axis=1).values, train_class)
            accuracy = SCORERS['accuracy'](pipeline, test.drop('class', axis=1).values, test_class)
            result.append(accuracy)

        for index, value in enumerate(result):
            print("Fold {:02d} score: {:.10f}".format(index + 1, value))

        print("Overall score: {:.10f}".format(sum(result) / self.__folds))

        return {"results": result, "average": sum(result) / self.__folds, "pipeline": pipeline}



def main():
    predictors = ["knn", "svm", "dt", "nb", "rf"]
    t = teapot(75, "E")
    scores = []

    for p in predictors:
        scores.append(t.score(p))

    sorted_scores = sorted(scores, key=lambda x: x['average'], reverse=True)
    print("\nBest values according to average scores")
    for s in sorted_scores:
        print("Average: {:.10f}  Pipeline: {}".format(s['average'], s['pipeline']))

    

if __name__ == "__main__":
    main()