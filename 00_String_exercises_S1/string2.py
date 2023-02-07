import re as regex

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  returnString = s
  if len(s) >= 3:
    if returnString.endswith('ing'):
      returnString += 'ly'
    else:
      returnString += 'ing'
  
  return returnString

      
    



# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):

  # Returnerer et regex object, som indeholder span (en substring hvor søgeresultat forekommer.
  # Hvis søgeresultatet ikke findes returneres datatypen None eller NoneType)
  # Læg mærke til at regex er importeret oppe i toppen
  regexObject = regex.search('not.*bad', s)
  if regexObject != None:
    regexSpan = regexObject.span()
    s = s.replace(s[regexSpan[0]: regexSpan[1]], 'good')
  return s
  


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  aFront = ""
  aBack = ""
  if len(a) % 2 == 0:
    aFront = a[0: int(len(a) / 2)]
    aBack = a[int(len(a) / 2):]
  else:
    aFront = a[0: int(len(a) /2 + 1)]
    aBack = a[int(len(a) / 2 + 1):]
  if len(b) % 2 == 0:
    bFront = b[0: int(len(b) / 2)]
    bBack = b[int(len(b) / 2):]
  else:
    bFront = b[0: int(len(b) /2 + 1)]
    bBack = b[int(len(b) / 2 + 1):]
  return aFront + bFront + aBack + bBack  


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print (prefix + ' got: ' + got + ' expected: ' + expected)


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

main()