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
        return True
    else:
        return False
    

def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

palindrome_generator = infinite_palindromes()
for i in palindrome_generator:
    print(i)
    digits = len(str(i))
    if digits == 5:
        palindrome_generator.close()
        # use .close instead - throws StopIteration exception, which signals the end of a finite iterator.
        #palindrome_generator.throw(ValueError("We don't like large     #palindromes"))
    palindrome_generator.send(10 ** (digits))


