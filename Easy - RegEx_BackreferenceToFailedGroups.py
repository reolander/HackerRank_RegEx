Regex_Pattern = r"_________"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())