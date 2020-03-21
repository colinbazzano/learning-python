"""patterns

patterns are a powerful way to use Regex
to learn more
regex101.com
to practice
https://regexone.com/
"""

import re

pattern = re.compile(r'([a-zA-Z]).([a])')
string = 'search this inside of this text yo!'


a = pattern.search(string)
