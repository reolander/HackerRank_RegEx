import re

count = 0
for _ in range(int(input())):
    s = input()
    m = re.search(r'hackerrank', s, re.IGNORECASE)
    if m:
        count += 1

print(count)

