import collections


def find_it(seq):
    occurrences = collections.Counter(seq)
    fin = []
    print(occurrences)
    for i in occurrences:
        if occurrences[i] % 2 != 0:
            fin.append(i)
    print(fin[0])


import re

txt = "The rain in Spain"
bxt = "Nobody has gone to America"
x = re.search("^The.*Spain$", txt)
j = re.search("^The.*Spain$", bxt)
#print(x.group())
#print(j)


lr = "lorm lorm b lomr z lorm b lrom b lrom b"
z = re.findall('b',lr)
#print(z)

d = re.split('z', lr)
#print(d)


from collections import Counter
from collections import defaultdict

listso = [1,2,3,4,5,6,6,7,2,2,5,1]

cnt = Counter(listso)

#print(cnt)
#print(cnt[1])
#print(list(cnt.elements()))
#print(list(cnt.most_common()))


nums = defaultdict(int)

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

#for key, value in od.items():
 #   print(key, value)


myset = set(["a", "b", "c"])
thatset = {'d','e','f','g'}
myset.add('0')
#print(myset)
myset.update(thatset)
#print(myset)
taco = {'d','z','f','j'}

#goldenfinger  = myset.union(taco)
goldFish = myset.intersection(taco)
google = myset.difference(taco)
#print(goldenfinger)
#print(goldFish)
#print(google)




jabba = ('Luke', 'Han', 'Vader')
theHutt = enumerate(jabba)

#print(list(theHutt))







