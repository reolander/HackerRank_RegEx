import re 

for _ in range(int(input())):
    s = input()
    m = re.search(r'^(\d{1,3})([-\s])(\d{1,3})\2(\d{4,10})$', s)
    print('CountryCode=' + m.group(1) + ',' + 'LocalAreaCode=' + m.group(3) + ',' + 'Number=' + m.group(4))
