import re

for _ in range(int(input())):
    s = input()
    res = re.search(r'^[Hh][Ii]\s[^Dd]', s)
    if res:
        print(s)

