# # 1. WAP to print numbers from 1 to 10 using a for loop.
# for i in range(11):
#     print(i)
# # 2. WAP to print numbers from 10 to 1 using a for loop.
# for i in range(10,0,-1):
#     print(i,end=" ")
# 3. WAP to print all even numbers from 1 to 50.
# li=[]
# for i in range(1,50):
#     if(i%2==0):
#         li.append(i)
# print(li)
# 4. WAP to print all odd numbers from 1 to 50.
# li = []
# for i in range(1,50):
#     if(i%2 !=0):
#         li.append(i)
# print(li)       
# 5. WAP to print numbers from 1 to 100 that are divisible by 5.
# li=[]
# for i in range(5,50,5):
#     li.append(i)
# print(li)

# # 6. WAP to print numbers from 1 to 100 that are divisible by both 3 and 5.
# for i in range(1,50):
#     if(i%3==0 and i%5==0 ):
#         print(i)
# # 7. WAP to print all prime numbers from 1 to 50.

# # 8. WAP to print the table of 7.
# for i in range(7,71,7):
#     print(i,end=" ")

# # 9. WAP to print the square of numbers from 1 to 10.
# for i in range(1,11):
#     i=i*i
#     print(i,end="=")
# 10. WAP to print numbers from 100 to 50 in reverse.
# for i in range(50,0,-1):
#     print(i,end=" ")

# # 11. WAP to create a list of 5 integers and print each using a for loop.
# li=[1,2,3,4,5,6,7,8,9]
# for i in li:
#     print(i)
# # 12. WAP to create a list of 5 floats and print each using a for loop.
# li=[10.2,12.4,54.3,65.2]
# for i in li:
#     print(i)
# 13. WAP to create a list of 10 numbers and print only even numbers.
# li=[]
# for i in range(10):
#     if(i%2==0):
#         li.append(i)
# print(li)
# 14. WAP to create a list and print only the odd numbers using a for loop.
# li=[]
# for i in range(10):
#     if(i%2 !=0 ):
#         li.append(i)
# print(li,end=" ")
# 15. WAP to find the sum of elements in a list.
# li=[1,2,3,4,5]
# sum=sum(li)
# print(sum)
# 16. WAP to find the maximum number in a list.
# li=[1,2,3,4,5]
# maximum=max(li)
# print(maximum)
# 17. WAP to find the minimum number in a list.
# li=[1,2,3,4,5]
# minimum=min(li)
# print(minimum)
# # 18. WAP to count even and odd numbers in a list.
# list=[1,2,3,4,5,6,7,8]
# even=[]
# odd=[]
# for i in list:
#     if(i % 2 ==0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(len(even),len(odd))

# 19. WAP to separate even and odd numbers from a list.
# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# even=[]
# odd=[]
# for i in list:
#     if(i % 2 == 0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(even,odd)
# 20. WAP to print the index and value of each element in a list using a loop.
# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# for i in range(len(list)):
#     print("index",i,"value",list[i])
# 21. WAP to create a dictionary of 5 items and print all key-value pairs.
# dict1={"name":"Soham","year":"BE","collage":"ACEM","blood group":"A+"}
# for i in dict1.items():
#     print(i)

# # 22. WAP to print only the keys from a dictionary.
# dict1={"name":"Soham","year":"BE","collage":"ACEM","blood group":"A+"}
# for i in dict1.keys():
#     print(i)
# 23. WAP to print only the values from a dictionary.
# dict1={"name":"Soham","year":"BE","collage":"ACEM","blood group":"A+"}
# for i in dict1.values():
#     print(i)
# 24. WAP to check if a key exists in a dictionary.
# dict1 = {"name": "Soham", "year": "BE", "collage": "ACEM", "blood group": "A+"}

# key_to_check = "year"

# if key_to_check in dict1:
#     print(f"Key '{key_to_check}' exists in the dictionary.")
# else:
#     print(f"Key '{key_to_check}' does not exist in the dictionary.")
# # 25. WAP to find the length of a dictionary.
# dict1 = {"name": "Soham", "year": "BE", "collage": "ACEM", "blood group": "A+"}
# print(len(dict1))
# 26. WAP to update a value for a specific key in a dictionary.
dict1 = {"name": "Soham", "year": "BE", "collage": "ACEM", "blood group": "A+"}
dict1.update({"year":"TE"})
print(dict1)
# 27. WAP to remove a key-value pair from a dictionary.
dict1.popitem()
print(dict1)
# 28. WAP to add a new key-value pair to an existing dictionary.
dict1.setdefault("gender","Male")
print(dict1)
# 29. WAP to iterate through a nested dictionary.
dict={1,2,3,4,100}
print(dict)
# 30. WAP to create a dictionary from two lists using a loop.
list1=["name", "year", "collage","blood group"]
list2=["Soham", "BE", "ACEM","A+"]
dict1={}
for i in range(len(list1)):
    dict1[list1[i]] = list2[i]
print(dict1)


# 31. WAP to count the number of digits in a number.
# 32. WAP to reverse a number using a loop.
# 33. WAP to print the factorial of a number using a for loop.
# 34. WAP to check if a number is a palindrome.
# 35. WAP to calculate the sum of digits of a number.
# 36. WAP to find the product of digits in a number.
# 37. WAP to print the Fibonacci series up to n terms.
# 38. WAP to print all numbers between 1 and 100 that are divisible by 3 or 7.
# 39. WAP to print all numbers divisible by 11 but not by 2 between 1 and 100.
# 40. WAP to print ASCII values of characters from A to Z using a for loop.
# 41. WAP to print list elements in reverse order using a loop.
# 42. WAP to calculate the average of numbers in a list.
# 43. WAP to remove duplicate elements from a list.
# 44. WAP to merge two lists into a single list.
# 45. WAP to sort a list in ascending order using a loop.
# 46. WAP to find the second largest number in a list.
# 47. WAP to find the second smallest number in a list.
# 48. WAP to rotate a list to the right by 1 position.
# 49. WAP to count occurrences of each element in a list using a dictionary.
# 50. WAP to create a list of 10 random numbers between 1 to 100.
