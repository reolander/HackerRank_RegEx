import re

l = []
n = int(input())
for _ in range(n):
  l.append(input())


for _ in range(int(input())):
  count = 0
  query = '\B' + input() + '\B'
  for s in l: 
    pattern = re.compile(query)
    res = pattern.findall(s)
    count += len(res)
  print(count)
