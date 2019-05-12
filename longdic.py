from pprint import pprint

dic = {}

c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l = 'abcdefghizklmnopqrstuvwxyz'
cap = list(c)
lit = list(l)

for i in range(len(c)):
    dic[c[i]] = l[i]
pprint(dic)