import re

l = []
for _ in range(int(input())):
    l.append(input())
s = ''.join(l)

d, m = {}, []
res = re.findall(r'(?:<\s*([a-zA-Z\d]+)[^>]*>|<\s*([a-zA-Z\d]+)[^>]*/>)', s)

if res:
    for r in res:
        for i in r:
            if i != '' and not d.get(i):
                d[i] = 1
                m.append(i)
m.sort()
print(';'.join(m))
