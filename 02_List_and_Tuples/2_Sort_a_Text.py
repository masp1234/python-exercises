

def removeVowelsAndSortAlphabetically(string):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'æ', 'Æ', 'ø', 'Ø', 'å', 'Å']
    for vowel in vowels:
        string = string.replace(vowel, "")
    
    return sorted(string)

print(removeVowelsAndSortAlphabetically("ollehE"))