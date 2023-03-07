
#Assignment 1
boardOfDirectors = { 'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = { 'Tine', 'Trunte', 'Rane'}
employees = { 'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

#who in the board of directors is not an employee?
not_employee = boardOfDirectors - employees
print(not_employee)

#who in the board of directors is also an employee?
employed_directors = boardOfDirectors.intersection(employees)
print(employed_directors)

#how many of the management is also member of the board?
directors_in_management = boardOfDirectors.intersection(management)
print(len(directors_in_management))

#All members of the managent also an employee
employed_managers = employees.intersection(management)
print(employed_managers)

#All members of the management also in the board?
managing_directors = boardOfDirectors.intersection(management)
print(managing_directors)

#Who is an employee, member of the management, and a member of the board?
employed_managing_directors = boardOfDirectors.intersection(management.intersection(employees))
print(employed_managing_directors)

#Who of the employees is neither a member or the board or management?
on_the_ground_employees = employees - (management | boardOfDirectors)
print(on_the_ground_employees)


#Assignment 2

#Using a list comprehension create a list of tuples from the folowing datastructure
#{‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}

input = {'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}

output = [(key, value) for key, value in input.items()]
print(output)

#Assignment 3
#From these 2 sets:
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

#Union
union = set1 | set2
print(union)

#Symmetric Difference
symmetric_difference = set1 ^ set2
print(symmetric_difference)

#Difference
difference = set1 - set2
print(difference)

#disjoint 
disjoint =  set1 & set2
print(disjoint)


#Assignment 4
#Date Decoder.
#A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
#Create a dict suitable for decoding month names to numbers.
months = {
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

#Create a function which uses string operations to split the date into 3 items using the "-" character.
#Translate the month, correct the year to include all of the digits.
#The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).
date_to_decode = '8-MAR-85'

def date_decoder(date_to_decode):
    day, month, year = date_to_decode.split('-')
    month_number = months[month]
    year_digits = '19' + year 
    return (int(year_digits), month_number, int(day)) # ( y , m , d )

date_now_decoded = date_decoder(date_to_decode)
print(date_now_decoded)

