import re


l= []
for _ in range(int(input())):
  l.append(input())
s = ' '.join(l)

for _ in range(int(input())):
  val = input()
  val2 = re.sub(r'our', 'or', val)

  res = re.findall(r'\b(%s|%s)\b'%(val, val2), s)
  print(len(res))
