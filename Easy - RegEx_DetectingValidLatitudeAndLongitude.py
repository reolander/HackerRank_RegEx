import re

for _ in range(int(input())):
    s = input()
    res = re.search(r'^\(([+-]?)(90(\.0+)?|[0-8]?[0-9](\.\d+)?),\s[+-]?(180(\.0+)?|([1][0-7][0-9]|[0-9]?[0-9])(\.\d+)?)\)$', s)
    print('Valid' if res else 'Invalid')
