samples = [
    (2001, 23),
    (2002, 7),
    (2002, -12),
    (2001, 21),
    (2003, 20),
    (2005, 13),
    (2003, 3),
    (2005, -2),
    (2003, 22),
    (2001, -3),
]
dic = {}



a = {}
for s in samples:
    # l = []
    if a.get(s[0]) is not None:
        lst = a[s[0]]
        lst.append(s[1])
#         # print(/b)
#         print(b)
#         # l.append(a[s[0]])
#         # l.append(s[1])
#         # a[s[0]] = l
    else:
        a[s[0]] = s[1]
print(a)
print(type(a.get(s[0])))
b = a.get(s[0])
b.append('1')
print(b)
# key값 담기, set함수 쓰기

samples.sort()
lst = []
for i in samples:
    lst.append(i[0])
setkey = set(lst)

# value값 담기
vals = []
for k in setkey:
    val = []
    for s in samples:
        if k in s:
            val.append(s[1])
    vals.append(val)

# 새로운 dictionary 만들기
for i, s in enumerate(setkey):
    dic[s] =  vals[i]

# 결과 print할 dictionary 만들기
dics = {}
for i in dic.items():
    maxval = max(i[1])
    dics[i[0]] = maxval
print(dics)
