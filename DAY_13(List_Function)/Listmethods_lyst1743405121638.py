# append  clear pop insert index count Extend remove reversed len copy del sort 

# Add data in list 
List1 = [10,20,30,100,25,30]
# Append()
        #   Add element End of the list
# print("Orignal list : ", List1)
# print("use append Method : ",List1.append(225))
# print("use append Method : ",List1.append(335))
# print("use append Method : ",List1.append([1,2,3]))
# print("Orignal list : ", List1)


# insert ()
# print("Orignal list : ", List1)
# print("use insert Method : ",List1.insert(2,225))
# print("use insert Method : ",List1.insert(0,335))
# print("use insert Method : ",List1.insert(3,[1,2,3]))
# print("Orignal list : ", List1)

# Extend()
# list2 = [220,320,420]
# print("Orignal list : ", List1)
# print("use Extend Method : ",List1.extend([1,2,3]))
# print("use Extend Method : ",List1.extend(list2))
# print("Orignal list : ", List1)

# sort and Sorted
# print("Orignal list : ", List1)
# # print("use sort Method : ",List1.sort(reverse=True))
# print("use Sotrtd Method : ",sorted(List1,reverse=True))
# print("Orignal list : ", List1)

#reverse and reversed 
# print("Orignal list : ", List1)
# # print("use reverse Method : ",List1.reverse())
# print("use reversed Method : ",tuple(reversed(List1)))
# print("Orignal list : ", List1)

# # Count 
# print("Orignal list : ", List1)
# print("use Count Method : ",List1.count(10))

# len 
# print("Orignal list : ", List1)
# print("use len Method : ",len(List1))

# Copy
# print("Orignal list : ", List1)
List3 = List1.copy()
# print("use copy Method : ",List3)

# #index
# print("Orignal list : ", List1)
# print("use index Method : ",List1.index(25))

#update element in list
# print("Orignal list : ", List1)
# List1[2] = 1000
# print("Orignal list : ", List1)


# # pop
# print("Orignal list : ", List1)
# print("use pop Method : ",List1.pop(30))
# print("Orignal list : ", List1)

# # remove
# print("Orignal list : ", List1)
# print("use remove Method : ",List1.remove(3000))
# print("Orignal list : ", List1)

# del
# print("Orignal list : ", List1)
# del List1[3]
# print("Orignal list : ", List1)


# clear
# print("Orignal list : ", List1)
# print("use clear Method : ",List1.clear())
# print("Orignal list : ", List1)
list4 = List1
print(id(list4))
print(id(List1))
print(id(List3))

