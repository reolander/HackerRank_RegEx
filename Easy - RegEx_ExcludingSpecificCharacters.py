Regex_Pattern = r'^\D[^aeiou][^bcdDF]\S[^AEIOU][^.,]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())