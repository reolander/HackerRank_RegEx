import re


l= []
for _ in range(int(input())):
  l.append(input())
s = ' '.join(l)

for _ in range(int(input())):
  val = input()
  val2 = ''
  if val[len(val)-2] == 's':
    val2 = val[:-2] + 'ze'
  elif val[len(val)-2] == 'z':
    val2 = val[:-2] + 'se'
  res = re.findall(r'(%s|%s)'%(val, val2), s)
  print(len(res))
