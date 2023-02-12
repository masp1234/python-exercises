import re as regex

# 4.1 Count the number of characters including blank spaces.

s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'

print(len(s))

# 4.2 Count the number of characters excluding blank spaces.
splitStr = s.split(' ')
newString = ''.join(splitStr)
newString = newString.strip()

print(len(newString))


# kan skrive ' '.join(string) hvis man vil have mellemrum 
# newString = ' '.join(splitStr)


# 4.3 Count the number of words.
print(len(regex.split(r' |\n\n', s)))