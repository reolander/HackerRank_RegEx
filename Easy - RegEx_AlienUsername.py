import re

for _ in range(int(input())):
    s = input()
    res = re.search(r'^[_.]\d+[a-z]*_?$', s, re.IGNORECASE)
    print('VALID' if res else 'INVALID')

