import re

for _ in range(int(input())):
    s = input()
    res = re.search(r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}', s)
    print('VALID' if res else 'INVALID')

