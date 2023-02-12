tuples = [(1, 2), (2, 2), (3, 2), (2, 1), (2, 2),
          (1, 5), (10, 4), (10, 1), (3, 1)]



sortedList = sorted(sorted(tuples, key=lambda x: x[0]), key=lambda x: x[1])

print(sortedList)

""" 
et nemmere overblik over hvad der sker

sortedList2 = sorted(tuples, key=lambda x: x[1])
sortedList3 = sorted(sortedList2, key=lambda x: x[0])
print(sortedList2)
print(sortedList3) 
"""
