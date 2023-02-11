array = ['Hello', 'World', 'Houston', 'we', 'are', 'here']
newArray = array[1:5]
print(newArray)


newArray2 = array[0:2]
print(newArray2)

newArray3 = array[4:]
print(newArray3)

newArray4 = array[4:5]
print(newArray4)

newArray5 = array[::2]
print(newArray5)

newArray6 = array[::-1]
# En anden måde, ved brug af 2 built in functions
newArray6_2 = list(reversed(array))
print(newArray6)
print(newArray6_2)

newArray7 = array[1:5]
print(newArray7)

newArray8 = array[1:4]
print(newArray8)