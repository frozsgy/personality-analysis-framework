import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
"""
l = [1, 0, 0, 1, 5, 1, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
vector = np.array(l)
v2 = np.array(l)
v3 = np.array(l)
print(vector)

finished = np.array(l)
finished = np.add(finished, v2)
finished = np.add(finished, v3)
r = ""
for i in finished:
	r += str(i) + " "
print(r)

vector = vector.reshape(-1, 1)

r = ""
for i in vector:
	r += str(i) + " "

print(r)"""

l = [ 37 , 41 , 35  ,31 ,654, 116, 274, 103 , 65  ,35  , 0 , 10 , 32 , 10,  25,  33 , 33,   2,  25  , 0]


"""[self.__morning, self.__afternoon, self.__evening, self.__night, 
self.__word, self.__verb, self.__noun, self.__punctuation, 
self.__adjective, self.__adverb, self.__negative, self.__numeral, 
self.__determiner, self.__conjunction, self.__pronoun, self.__incorrect, 
self.__plural, self.__full_stop, self.__smiling_emoji, self.__negative_emoji]"""

coeff = [1., 1., 1., 1.,
20., 3., 11., 5.38,
2.5, 1.5, 0.33, 2.06,
1., 1., 1.23, 6.58,
3.52, 0.91, 1., 0.06]

lf = l
vector = np.array(lf)
vector = vector.reshape(-1, 1)

est = KBinsDiscretizer(n_bins=[4], encode='ordinal').fit(vector)
j = est.transform(vector)



r = ""
for i in j:
	r += str(i) + " "

print(r)

k = j.reshape(1, 20)


print("-"*80)
print("coefficients: ")
print(coeff)
print("original: ")
print(k)

kk = k/4.
print("divided 4: ")
print(kk)


k = k/3.
print("divided: ")
print(k)




t = np.multiply(kk, np.array(coeff))
print("multiplied: ")
print(t)
