
# 3.1 create a list with names
names = ['Claus', 'Ib', 'Per', 'Bob', 'Dude']

# 3.2 sort list by using sorted() build in function
print(sorted(names))


# 3.3 sort the list in reverse order
print(sorted(names, reverse=True))

# 3.4 sort the list by length of the names
print(sorted(names, key=len))

# 3.5 sort the list based on the last letter in the name
def reverseWord(str):
    return str[::-1]

print(reverseWord('hello'))
print(sorted(names, key=reverseWord))

# en federe måde, vha. en lambda function
# lidt det samme som en arrow function: lambda keyword, x er parameteret og x[::-1] er det som returneres, som her er x baglæns
print(sorted(names, key=lambda x: x[::-1]))


# 3.6 sort the list based on when "a" appears in a name


print(names)
# alle dem som ikke har a i navnet kommer først, da s.find('a') returnerer -1 når der ikke bliver fundet noget 'a' i stringen
print(sorted(names, key=lambda s: s.find('a')))

# virker ikke, da 'a' ikke forekommer i alle navne
# print(sorted(names, key=lambda x: x.index('a')))

