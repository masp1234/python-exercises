def is_palindrome(num):
    # Skip single-digit inputs
    # "//" is floor division. example: 75 // 10 will be 7, since it rounds the result down to the nearest whole number
    if num // 10 == 0:
        return False
    original_number = num
    reversed_num = 0

    while original_number != 0:
        reversed_num = (reversed_num * 10) + (original_number % 10)
        original_number = original_number // 10

    if num == reversed_num:
        return num
    else:
        return False
    

def infinite_sequence():
    num = 0
    while True:
        yield num
        if num == 10000:
            break
        num += 1

for number in infinite_sequence():
    palindrome = is_palindrome(number)
    if palindrome:
        print(palindrome)
    