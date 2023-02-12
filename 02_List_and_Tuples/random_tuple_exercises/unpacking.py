# https://www.datacamp.com/tutorial/python-tuples


us_cookies = ['Chocolate Chip', 'Brownies', 'Peanut Butter', 'Oreos', 'Outmeal Raisin']

india_cookies = ['Punjabi', 'Fruit Cake Rusk', 'Marble Cookies', 'Kaju Pista Cookies', 'Almond Cookies', 'random cookie']

# skal returnere som en liste, tuple eller andet, ellers får man bare: <zip object at 0x000001C465AF2280> printet ud
# læg mærke til at den kun zipper par sammen -> 'random cookie' bliver ignoreret
top_pairs = tuple(zip(us_cookies, india_cookies))

us_num_1, in_num_1 = top_pairs[0]
print(us_num_1)
print(in_num_1)

print('For loop der bruger tuple unpacking')
for us_cookie, in_cookie in top_pairs:
    print(us_cookie)
    print(in_cookie)

