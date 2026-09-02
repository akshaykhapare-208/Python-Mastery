# STRING FUNCTION

name = "Akshay"

# 1. len() returns the length of the string.
print(len(name))   # Ouput : 6

# 2. endswith() checks if a string ends with given text.
print(name.endswith("hay")) # Output : True

# 3. count() counts total occurrences of a character
print(name.count("s")) # Output: 1

# 4. capitalize() capitalizes the first character
print(name.capitalize) # Output : AKSHAY

# 5. find() returns the index of first occurrence
print(name.find("sh")) # Output : 2

# 6. replace(old word, new word) replaces the old word with the new word in the string.
print(name.replace("s" , "h"))  # Output : Akhhay

# Sequence of characters after backslash "\" are called Escape Sequence characters.

print("Hello My Name \n is Akshay") #newline
print("Hello My Name \t is Akshay") #tab Space
print("Hello My Name \' is Akshay") #Add Single Quote
print("Hello My Name \\ is Akshay") #Add Backshalsh

