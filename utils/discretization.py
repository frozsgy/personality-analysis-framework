import numpy as np


class Discretizer:

    __first_quartile = None
    __mean = None
    __third_quartile = None
    __features = []
    __discretized = []

    def __init__(self, arr):
        self.__features = arr
        self.__first_quartile, self.__mean, self.__third_quartile = np.percentile(arr, [25, 50, 75])

    def discretize(self):
        for i in self.__features:
            if i <= self.__first_quartile:
                self.__discretized.append(0.0)
            elif i <= self.__mean:
                self.__discretized.append(0.25)
            elif i <= self.__third_quartile:
                self.__discretized.append(0.75)
            else:
                self.__discretized.append(1.0)

    def get_discretized(self):
        if len(self.__discretized) == 0:
            self.discretize()
        return self.__discretized
