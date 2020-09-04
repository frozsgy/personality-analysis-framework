
from numpy import array
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


class Predict:

    def __init__(self):

        data = eval(open("predictors/vectors", "r").read())

        self.__vector = []
        self.__gt = {'o': [], 'c': [], 'e': [], 'a': [], 'n': []}

        for key, value in data.items():
            self.__vector.append(value['twitter'])
            for personality in "ocean":
                self.__gt[personality].append(value['personality'][personality])

        self.__X = array(self.__vector)
        self.__y_o = array(self.__gt['o'])
        self.__y_c = array(self.__gt['c'])
        self.__y_e = array(self.__gt['e'])
        self.__y_a = array(self.__gt['a'])
        self.__y_n = array(self.__gt['n'])

    def predict_openness(self, guess):
        predictor = DecisionTreeClassifier(criterion='entropy', max_depth=5, min_samples_leaf=17, min_samples_split=8)
        predictor.fit(self.__X, self.__y_o)
        return predictor.predict([guess])

    def predict_conscientiousness(self, guess):
        predictor = DecisionTreeClassifier(max_depth=5, min_samples_leaf=20, min_samples_split=10)
        predictor.fit(self.__X, self.__y_c)
        return predictor.predict([guess])

    def predict_extraversion(self, guess):
        predictor = LinearSVC(C=0.1, loss='hinge', tol=0.1)
        predictor.fit(self.__X, self.__y_e)
        return predictor.predict([guess])

    def predict_agreeableness(self, guess):
        predictor = KNeighborsClassifier(n_neighbors=10, p=1, weights='distance')
        predictor.fit(self.__X, self.__y_a)
        return predictor.predict([guess])

    def predict_neuroticism(self, guess):
        predictor = LinearSVC(dual=False, penalty='l1', tol=0.001)
        predictor.fit(self.__X, self.__y_n)
        return predictor.predict([guess])

    def predict(self, guess):
        r = dict()
        r['o'] = self.predict_openness(guess)[0]
        r['c'] = self.predict_conscientiousness(guess)[0]
        r['e'] = self.predict_extraversion(guess)[0]
        r['a'] = self.predict_agreeableness(guess)[0]
        r['n'] = self.predict_neuroticism(guess)[0]

        return r



"""

d = [-0.06502657617225369, -0.04034071140999233, 0.3766550744364455, -0.048243234285002344, -0.15439208869548507, 0.014398935547696792, 0.12933753171216536, -0.055518233893284495, -0.13731515688138812, 0.16936441573628053, 0.04882539989273589, 0.16286689358212822, 0.2671018440463528, -0.1072647876596978, -0.20504306588840912, 0.02725152418548124, -0.36436579129160107, 0.10802993914069074, 0.13698691477122796, -0.1577423212146454, 0.01215057302197883, -0.1177607247435891, -0.13028707828505795, -0.022411355004128542, -0.1664820652190969, -0.11195304914393434, -0.10723765625079501, -0.33191350633049793, -0.007305266276462934, -0.0894706530350565, 0.09708195105934514, -0.10181338655057068, -0.04802176473357528, -0.19020990861668458, 0.2395179424221524, -0.4375375143707725, -0.0013424275690524644, 0.15886655959017248, 0.75, 0.75, 0.25, 0.75, 1.0, 1.0, 1.0, 1.0, 1.0, 0.25, 0.0, 0.25, 0.25, 0.0, 0.25, 0.0, 0.75, 0.75, 0.0, 0.0]
d = [-0.055027552203480434, -0.03820802897668911, 0.28169682184835887, -0.0302483474451956, -0.13990119657436229, 0.02100796652571855, 0.1115160091640401, -0.08548269626735248, -0.0807035660539135, 0.16806850083254019, 0.04781100594722457, 0.0874925911543364, 0.25457510551717305, -0.08448491411340071, -0.17369424339407294, 0.011737863006425644, -0.22289607439290257, 0.09134468728643781, 0.16734401385634148, -0.13139155990387041, 0.1298809082866671, -0.07850595134057524, -0.062318089529659705, 0.007399189169502478, -0.13490682673428342, -0.08687284580716277, -0.13280875531376915, -0.2407283310603312, 0.020081358151262305, -0.06321890085419013, 0.12662599506659808, -0.08849463601621387, -0.11775285151757138, -0.11340774732171259, 0.14615018960307635, -0.3284291602044744, -0.014178179536904941, 0.18666309606703266, 0.75, 0.25, 0.25, 0.75, 1.0, 1.0, 1.0, 1.0, 1.0, 0.75, 0.0, 0.25, 0.0, 0.0, 0.0, 0.25, 0.75, 0.75, 0.0, 0.0]

p = Predict()

print(p.predict(d))


"""