# Write a Python program to convert the given string "hello world" to uppercase.
str1="hello world"
print("UpperCase is :",str1.upper())

# Convert the string "Python Programming" to lowercase.
str1="Python Programming"
print("LowerCase is :",str1.lower())

# Capitalize the first letter of "hello python learners".
str1="hello python learners"
print("Capitalize the first letter :",str1.capitalize())

# Convert "welcome to python" to title case.
str1="welcome to python"
print("Convert : ",str1.title())
# Remove leading and trailing spaces from the string " Python String Functions " using strip().
str1=" Python String Functions "
print(str1.rstrip()) 
print(str1.lstrip()) 
# 	6. Remove only trailing spaces from 
str1="Hello World "
print(str1.strip()) 
# 	7. Remove only leading spaces from " Learn Python".
str1=" Learn Python"
print(str1.lstrip()) 
# 	8. Split the string "apple banana grape" into a list using split().
str1="apple banana grape"
print(str1.split())
# 	9. Join the list ['Python', 'is', 'fun'] into a single string using join() with space as a separator.
l1= ['Python', 'is', 'fun'] 
print(" ".join(l1))
#        10. Convert the list ['A', 'B', 'C'] into a single string "A-B-C" using join().
list1= ['A', 'B', 'C']
print("-".join(list1))
#        11. Find the index of the first occurrence of "Python" in "I love Python programming".
str1="I love Python programming"
print("index of python :",str1.index("Python"))
#        12. Find the last occurrence of "o" in "Hello World".
str1 = "Hello World"
print("Occurance Of o :",str1.count("o"))
#        13. Replace "Java" with "Python" in the string "I love Java".
str1 = "I love Java"
print("Replace :",str1.replace("Java","Python"))
#        14. Check if the string "Hello World" starts with "Hello".
str1="Hello World"
print("Check if the string :",str1.startswith("Hello"))
#        15. Check if the string "example.txt" ends with ".txt".
str1="example.txt"
print("Check if the string",str1.endswith(".txt"))
#        16. Count the occurrences of "o" in "Hello, how are you?".
str1="Hello, how are you?"
print(" Count the occurrences of o :",str1.count("o"))
#        17. Find the index of "r" in "programming".
str1="programming"
print("Find the index of r : ",str1.index("r"))

#       18. Try finding the index of "z" in "python" using index(), and observe the error.
str1="python"
print("finding the index of z :",str1.index("z"))
#       19. find the last occurrence of "e"(( in "experience".
str1="experience"
print("the last occurrence of e :",str1.index("e"))
#       20. find the first occurrence of "e" in "experience".
str1="experience"
print("the first occurrence of e",str1.index("e"))
#       21. Check if the string "Python" contains only alphabets.
str1="Python"
print("if the string Python contains only alphabets : ",str1.isalpha())
#       22. Verify if "12345" contains only digits.
str1="12345"
print("12345 contains only digits :",str1.isalnum())
#       23. Check if "Python123" is alphanumeric.
str1="Python123"
print("Python123 is alphanumeric",str1.isalnum())
#       24. Test if the string " " consists of only spaces.
str1=" "
print(" consists of only spaces :",str1.isspace())
#       25. Check if "12345" is numeric using.
str1="12345"
print("is numeric :",str1.isnumeric())
#       26. Use format() to insert "Python" and "fun" into the string "{} is {}!".
str1="Python"
print("fun into the string : ",str1.format("fun"))
#       27. Partition the string "python-programming-language" at "-".
str1="python-programming-language"
print("Partition the string :",str1.partition("-"))

#       28. Use rpartition() to split "one-two-three" from the right sing "-".
str1="one-two-three"
print(str1.rpartition("-"))
#       29. Convert "PYTHON" to lowercase using casefold().
str1="PYTHON"
print(str1.casefold()) 
#       30. Convert "42" into a 5-character string padded with zeros using zfill().
str1="42"
print(str1.zfill(5))
#       31. Check if "HELLO" is in uppercase.
str1="HELLO"
print(str1.isupper())
#       32. Verify if "hello" is in lowercase.
str1="hello"
print(str1.islower())
#       33. Check if "Python Programming" follows title case.
str1="Python Programming"
print(str1.istitle())
#       34. Sort the characters of "banana" alphabetically.
str1="banana" 
print(sorted(str1))
#       35. Find the length of the string "Data Science".
str1="Data Science"
print(len(str1))
#       36. Sort the characters of "The Kiran  Academy" alphabetically in descending Order.
str1="The Kiran  Academy" 
print(sorted(str1))