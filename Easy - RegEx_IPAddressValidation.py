import re


for _ in range(int(input())):
  s = input()
  ip4 = s.split('.')
  ip6 = s.split(':')
  if len(ip4) < 4:
    if len(ip6) < 8:
      print('Neither')
    elif len(ip6) == 8:
      for block in ip6:
        flag = 1
        res = re.search(r'^[a-fA-F0-9]{1,4}$', block)
        if not res:
          flag = 0
          print('Neither')
          break
      if flag:
        print('IPv6')
  elif len(ip4) == 4:
    flag = 1
    for byte in ip4:
      if int(byte) < 0 or int(byte) > 255:
        print('Neither')
        flag = 0
        break
    if flag:
      print('IPv4')


