"""patterns

patterns are a powerful way to use Regex
to learn more
regex101.com
to practice
https://regexone.com/

email validation r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

"""

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'fake_email@email.org'
pattern2 = re.compile(r"[a-zA-Z0-9$%#@]{8,}")
password = 'difaj$wEDJO%sjdi'
a = pattern.search(string)
print(a)
check = pattern2.fullmatch(password)

print(check)
# At least 8 char long
# contain any sort of letters, numbers, $%#@
