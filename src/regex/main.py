import re
string = 'search inside of this text, please!'


print('search' in string)

# we are looking for the word 'this' in the variable string
a = re.search('this', string)

# will show you where it began counted via index
print(a.start())
# returns what you wanted if available
print(a.group())


"""NoneType

if you cannot find the word, it will return a NoneType error, so you can except for it

you can do other methods such as

pattern = re.compile('text to be searched through')

a = pattern.search(string)
b = patternfindall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

"""
