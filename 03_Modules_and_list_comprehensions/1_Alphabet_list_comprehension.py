alphabet = [chr(l) for l in range(65, 91)]
print(alphabet)

capitalExclude = [chr(l) for l in range(65, 91) if l != 70 and l != 75 and l != 80 and l != 85]
print(capitalExclude)

capitalExclude2 = [chr(l) for l in range(65, 91) if l % 5 != 0]
print(capitalExclude2)

capitalExclude3 = [chr(l) for l in range(65, 91) if l not in [70, 75, 80, 85]]
print(capitalExclude3)

capitalExclude4 = [chr(l) for l in range(65, 91) if l not in range(70, 86, 5)]
print(capitalExclude4)


ex3 = [chr(l) for l in range(65, 91) if l not in range(70, 80, 2)]
print(ex3)


print(list(range(70, 80, 2)))

