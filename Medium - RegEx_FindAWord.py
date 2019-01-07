import re

l = [' ']
for _ in range(int(input())):
  l.append(input())
l.append(' ')
s = ' '.join(l)

for _ in range(int(input())):
  val = '(?<=\W)' + input() + '(?=\W)' 
  pattern = re.compile(val)
  res = pattern.findall(s)
  print(len(res))

