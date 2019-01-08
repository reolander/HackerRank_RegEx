import re

l = []
for _ in range(int(input())):
    l.append(input())
s = ' '.join(l)

res = re.findall(r'https?://(?:(?:[w]{3}\.)?|(?:w2\.)?)([\w-]+\.[\w.-]+)(?=(?:[/?"]))', s)

l = []
d = {}
for elm in res:
    if not d.get(elm):
        l.append(elm)
        d[elm] = 1

l.sort()
print(';'.join(l))

