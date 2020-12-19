a=input((print("введите 1 слово ")))
d={}
for x in set(a):
    d[x]=a.count(x)
print(d)
