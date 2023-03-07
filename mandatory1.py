# Assignment 1 :

# Model an organisation of employees, management and board of directors in 3 sets.
# Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren
# Management: Tine, Trunte, Rane
# Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

board_of_directors = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
management = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}


# who in the board of directors is not an employee?
not_employees = board_of_directors - employees
print(not_employees)

# who in the board of directors is also an employee?
board_of_directors_employees = board_of_directors & employees
print(board_of_directors_employees)

# how many of the management is also member of the board?
count = len(management & board_of_directors)
print(count)

# All members of the managent also an employee :
if management.issubset(employees):
    print("All members of the management are also employees.")
else:
    print("Not all members of the management are employees.")

# All members of the management also in the board :
if management.issubset(board_of_directors):
    print("All members of the management are also in the board of directors.")
else:
    print("Not all members of the management are also in the board of directors.")

# Who is an employee, member of the management, and a member of the board?
result = employees.intersection(management, board_of_directors)
print("Employees who are also in the management and the board of directors : ")
print(result)

# Who of the employee is neither a member of the board or in the management?
result = employees.difference(management,board_of_directors)
print("employees who are neither in the management or are a member of the board: ")
print(result)


#Assignment 2 :
#2.	Using a list comprehension create a list of tuples from the folowing datastructure
#{‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}
d = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
# Our iterable is represented by the d.items(), which returns a tuple of tuples of our key value pairs.  We iterate over these by creating a new tuple of the key-value pairs.
tuples_list = [(k, v) for k, v in d.items()]
print(tuples_list)
# result :
[('a', 'Alpha'), ('b', 'Beta'), ('g', 'Gamma')]


# Assignment 3 :
# From these 2 sets:
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}
# Union:
union_set = set1.union(set2) # Combines the two sets into a new set that contains all unique elements from both sets.

print(union_set)

# Symmetric difference :
sym_diff_set = set1.symmetric_difference(set2) #The resulting set sym_diff_set will contain all the elements that are unique to either set1 or set2, but not present in both.
print(sym_diff_set)

# Difference :
diff_set = set1.difference(set2) #The resulting set diff_set will contain all the elements that are present in set1, but not in set2, in this case an empty set
print(diff_set)

# Disjoint :
disjoint_set = set1.isdisjoint(set2) # Returns true if the sets have no common elements.

print(disjoint_set)


# Assignment 4 :

def decode_date(date_str):
    # Create a dictionary for decoding month names to numbers
    month_dict = {"JAN": "01", "FEB": "02", "MAR": "03", "APR": "04",
                  "MAY": "05", "JUN": "06", "JUL": "07", "AUG": "08",
                  "SEP": "09", "OCT": "10", "NOV": "11", "DEC": "12"}
    # Split the date into 3 items using the "-" character
    day, month, year = date_str.split("-")
    # Translate the month
    month = month_dict[month]
    # Correct the year to include all of the digits
    year = "20" + year if int(year) <= 23 else "19" + year
    return (year, month, day)


print(decode_date('23-MAR-85'))

    


