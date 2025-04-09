# ## String Functions Practices ##

# 1. Write a Python program to convert the given string "hello world" to uppercase.
str1="hello world"
print(str1.upper())
#   2. Convert the string "Python Programming" to lowercase.
str1="Python Programming "
print(str1.lower())
# 3. Capitalize the first letter of "hello python learners".
str1="hello python learners"
print(str1.capitalize())
# 4. Convert "welcome to python" to title case.
str1="welcome to python" 
print(str1.title())
# 5. Remove leading and trailing spaces from the string " Python String Functions " using strip().
str1=" Python String Functions "
print(str1.strip())
# 6. Remove only trailing spaces from "Hello World " .
str1="Hello World " 
print(str1.rstrip())
# 7. Remove only leading spaces from " Learn Python".
str1=" Learn Python"
print(str1.lstrip())
# 8. Split the string "apple banana grape" into a list using split().
str1="apple banana grape"
print(str1.split())
# 9. Join the list ['Python', 'is', 'fun'] into a single string using join() with space as a separator.
str1=['Python', 'is', 'fun']
print(" ".join(str1))
#  10. Convert the list ['A', 'B', 'C'] into a single string "A-B-C" using join().
str1=['A', 'B', 'C']
print("-".join(str1))
#  11. Find the index of the first occurrence of "Python" in "I love Python programming".
str1="I love Python programming"
print(str1.count("Python"))
#  12. Find the last occurrence of "o" in "Hello World".
str1="Hello world"
print(str1.count("o"))
#  13. Replace "Java" with "Python" in the string "I love Java".
str1="I love Java"
print(str1.replace("Java","Python"))
#  14. Check if the string "Hello World" starts with "Hello".
str1="Hello World"
print(str1.startswith("Hello"))
#  15. Check if the string "example.txt" ends with ".txt".
str1="example.txt"
print(str1.endswith(".txt"))
#  16. Count the occurrences of "o" in "Hello, how are you?".

#  17. Find the index of "r" in "programming".
str1="programming"
print(str1.index("r"))
# 18. Try finding the index of "z" in "python" using index(), and observe the error.
#str1="python"
#print(str.index("z"))
# 19. find the last occurrence of "e" in "experience".
# 20. find the first occurrence of "e" in "experience".
# 21. Check if the string "Python" contains only alphabets.
str1="Python"
print(str1.isalpha())
# 22. Verify if "12345" contains only digits.
str1="12345" 
print(str1.isdigit())
# 23. Check if "Python123" is alphanumeric.
str1="Python123"
print(str1.isalnum())
# 24. Test if the string " " consists of only spaces.
# 25. Check if "12345" is numeric using.
# 26. Use format() to insert "Python" and "fun" into the string "{} is {}!".
# 27. Partition the string "python-programming-language" at "-".
# 28. Use rpartition() to split "one-two-three" from the right sing "-".
# 29. Convert "PYTHON" to lowercase using casefold().
# 30. Convert "42" into a 5-character string padded with zeros using zfill().
# 31. Check if "HELLO" is in uppercase.
# 32. Verify if "hello" is in lowercase.
# 33. Check if "Python Programming" follows title case.
# 34. Sort the characters of "banana" alphabetically.
# 35. Find the length of the string "Data Science".
# 36. Sort the characters of "The Kiran  Academy" alphabetically in descending Order.