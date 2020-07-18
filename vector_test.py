from vector import vector
from twitter import tweet

a = vector.Vector()
t = tweet.Tweet(1270766134439092230,"2020-06-10 17:13:50","gdfgfdsgdgsdf gfdsg",False)

print(a.get_vector())

a.set_time(t)

print(a.get_vector())