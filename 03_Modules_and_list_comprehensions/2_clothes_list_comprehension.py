colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
genders = ['male', 'female']

# for loop version
clothes = []
for color in colors:
    for size in sizes:
        clothes.append((color, size))

clothes_li_comprehension = [(color, size) for size in sizes for color in colors]
print(clothes_li_comprehension)
# list comprehension version med et ekstra element i tuplerne
clothes_li_comprehension_extra = [(color, size, gender) for size in sizes for color in colors for gender in genders]

print(clothes_li_comprehension_extra)

soldOut = [('Black', 'm'), ('White', 's')]

clothesInStock = [(color, size) for size in sizes for color in colors if (color, size) not in soldOut]
print('In Stock: ', clothesInStock)

# underlig syntax når man bruger else - slå det op
test = [i if i % 2 == 0 else 'Hello' for i in range(10)]
print(test)