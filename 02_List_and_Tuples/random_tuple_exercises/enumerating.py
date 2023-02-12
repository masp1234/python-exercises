# https://www.datacamp.com/tutorial/python-tuples


us_cookies = ['Chocolate Chip', 'Brownies', 'Peanut Butter', 'Oreos', 'Outmeal Raisin']

india_cookies = ['Punjabi', 'Fruit Cake Rusk', 'Marble Cookies', 'Kaju Pista Cookies', 'Almond Cookies', 'random cookie']

# skal returnere som en liste, tuple eller andet, ellers får man bare: <zip object at 0x000001C465AF2280> printet ud
# læg mærke til at den kun zipper par sammen -> 'random cookie' bliver ignoreret
top_pairs = tuple(zip(us_cookies, india_cookies))

"""
Another useful tuple creation method is the enumerate() function. Enumeration is used in loops to return the position and the data in that position while looping.

Example
Here we enumerate our top pairs list and split that resulting tuple into index idx and item
"""

for index, item in enumerate(top_pairs):
    us_cookie, in_cookie = item
    print(index, us_cookie, in_cookie)