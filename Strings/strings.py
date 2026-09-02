# String is a data type in python.
# String is a sequence of characters enclosed in quotes.
# We can primarily write a string in these three ways.

a = 'harry' # Single quoted string
b = "harry" # Double quoted string
c = '''harry''' # Triple quoted string

# A string in python can be sliced for getting a part of the strings.

name = "Akshay"
s = name [ 1 : 4]
print(len(name))
print(s)

word = "amazing"
word[1:6:2] # mzn Skiping Value 
word[-7:-1] # amazin
word[:7] # amazing
word[0:] # amazing