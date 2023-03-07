
# Exercise 1

directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}

management = {'Tine', 'Trunte', 'Rane'}

employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

notAnEmployee = directors.difference(employees)
print(notAnEmployee)

alsoAnEmployee = directors.intersection(employees)
print(alsoAnEmployee)

alsoMemberOfBoard = management.intersection(directors)
print(len(alsoMemberOfBoard))

alsoAnEmployee = management.intersection(employees)
print(alsoAnEmployee)

alsoMemberOfBoard2 = management.intersection(directors)
print(alsoMemberOfBoard2)

allThree = management.intersection(directors, employees)
print(allThree)

notMemberOfTheBoardOrManagement = employees.difference(directors, management)
print(notMemberOfTheBoardOrManagement)



# Exercise 2

dictionary = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
listOfTuples = [(key, value) for key, value in dictionary.items()]
print(listOfTuples)



# Exercise 3

vowels = {'a', 'e', 'o', 'u', 'y'}
danishVowels = {'a', 'e', 'o', 'u', 'y', 'æ', 'ø', 'å'}

union = vowels.union(danishVowels)
print(union)

symmetricDifference = vowels.symmetric_difference(danishVowels)
print(symmetricDifference)

difference = vowels.difference(danishVowels)
print(difference)

disjoint = vowels.intersection(danishVowels)
print(disjoint)



# Exercise 4

monthNameDecoder = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}

def dateDecoder(date):
    dateSplit = date.split('-')
    year = dateSplit[2]
    if int(year) > 23:
        year = '19' + year
    else:
        year = '20' + year

    return (year, str(monthNameDecoder[dateSplit[1]]), dateSplit[0])

print(dateDecoder('23-MAR-85'))
print(dateDecoder('1-DEC-23'))



