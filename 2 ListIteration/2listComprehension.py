# 列表解析

print([x * x for x in range(1, 11)])

print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
for i in L1:
    if isinstance(i,str) == False:
        L1.remove(i)
print([s.lower() for s in L1])


