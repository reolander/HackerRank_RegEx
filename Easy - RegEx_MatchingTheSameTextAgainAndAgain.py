Regex_Pattern = r'^([a-z]\w\s\W\d\D[A-Z][a-z,A-Z][aieouAEIOU]\S)\1$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())