import sys

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('size of the x list:', sys.getsizeof(x))
print('range(1, 11) iterator size:', sys.getsizeof(range(1, 11)))
# Range function returns an iterator. That's why the size stays the same regardless of the range. 1, 11 is same size as 1, 1000. Way better than storing the list in memory
print('range(1, 1000) iterator size:', sys.getsizeof(range(1, 1000)))

y = map(lambda i: i **2, x)
print('map iterator size:', sys.getsizeof(y))
