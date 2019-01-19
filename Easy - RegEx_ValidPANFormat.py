import re 

for _ in range(int(input())):
    s = input()
    res = re.search(r'^[A-Z]{5}\d{4}[A-Z]$', s)
    print('YES' if res else 'NO')

