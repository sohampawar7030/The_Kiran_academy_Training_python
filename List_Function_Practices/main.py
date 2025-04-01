# 									## List Method Practical ##

# 1. Create an empty list and use append() to add five different numbers to it. Print the final list.
list1=[]
list1.append(10)
list1.append(20)
list1.append(30)
print(list1)
# 2. Create a list of student name  and append a new Student name  and print the length of list .
student_name=[]
student_name.append("Soham")
student_name.append("Nilesh")
student_name.append("Omkar")
student_name.append("Sahil")
print(student_name)
print("length of the list is : ",len(student_name))
# 3. Append a list [10, 20, 30] to another list and observe the result.
l1=[1,2,3,4]
list2=[10,20,30]
l1.append(list2)
print(l1)

# 4. Create a list and make a copy using copy().
list1=[10,20,30]
list2=list1.copy()
print(list2)
# 5. Create a list with at least 10 elements, use clear(), and check the length of the list afterward.
List1=[1,2,3,4,5,6,7,8,9,0]
List1.clear()
print("Length of list is :",len(List1))
# 6. Create a nested list and clear only the inner list while keeping the outer list intact .
l1=[1,2,3,[10,20,30],4,5,6,[40,50,60],7,8,9,0]
print(l1)
print("Removing the Nested list After Output is :",l1.pop(3))
l1.pop(6)
print(l1)
# 7. Given nums = [1, 2, 3, 4, 2, 2, 5, 2], find how many times 2 appears in the list.
list1=[1, 2, 3, 4, 2, 2, 5, 2]
print(list1)
print("check occurance of 2 is :",list1.count(2))

# 8. Create a list of words and find how many times a particular word appears.
list1=[1, 2, 3, 4, 2, 2, 5, 2]
print(list1)
print("check occurance of 2 is :",list1.count(2))
# 9. Create two lists, list1 in integer variable  and list2 in String variable. Use extend() to add elements of list2 to list1. Print the final result.
list1=[1,2,3,5,6,7,9]
list2=['Soham', 'Nilesh', 'Omkar', 'Sahil']
list1.extend(list2)
print(list1)
# 10. Given fruits = ['apple', 'banana', 'cherry', 'banana', 'grape'], find the index of banana.
list1=['apple', 'banana', 'cherry', 'banana', 'grape']
print(list1)
print("position of banana is :",list1.index("banana"))
# 11. Insert the number 100 at the beginning of the list [10, 20, 30].
list1= [10, 20, 30]
print(list1)
list1.insert(0,100)
print(list1)
# 12. Insert 'Python' at index 2 in a list of programming languages and print the result.
list1=["c","c++","c#","Java"]
print(list1)
list1.insert(1,"Python")
print(list1)
# 13. Given numbers = [5, 10, 15, 20, 25], remove and print the last element using pop().
list1=[5, 10, 15, 20, 25]
list1.pop()
print(list1)
# 14. Remove an element at index 2 and print both the removed element and the updated list.
list1.pop(2)
print(list1)

# 15. Given colors = ['red', 'blue', 'green', 'blue', 'yellow'], remove the first occurrence of 'blue'.
colors=['red', 'blue', 'green', 'blue', 'yellow']
colors.pop(1)
print(colors)
# 16. Reverse the list [1, 4, 9, 16, 25] and print the result.
list=[1, 4, 9, 16, 25]
print(list)
print("Reverse list :",list.reverse())
print(list)


# 17. Reverse a list of words and join them to form a sentence words = ["Hello", "world", "Python"].
words = ["Hello", "world", "Python"]
words.reverse()  # Reverse the list in place
sentence = " ".join(words)  # Join the words to form a sentence
print(sentence)


# 18. Sort a list of numbers [10, 5, 8, 3, 1] in ascending and then in descending order.
list1 = [10, 5, 8, 3, 1]

# Sorting in ascending order
list1.sort()
print("Ascending order:", list1)

# Sorting in descending order
list1.sort(reverse=True)
print("Descending order:", list1)