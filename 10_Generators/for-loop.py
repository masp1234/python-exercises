letters = ['a', 'b', 'c', 'y']

iterator = iter(letters)

while True:
    try:
        letter = next(iterator)
    except StopIteration:
        break
    print(letter)