# Dictionary Data Structure :


dict1={"Name":"Soham","Year":4,"branch":"AIML","Univarsity":"SPPU","result":"Pass"}
dict2={"collage":"ACEM PUNE","Address":"Pune"}
list=[("Soham", "Pawar"),("Yes" ,"NO")]

print(list)
dict = dict(list)
print(dict)
print(type(dict))
# print(dict1)

# dict2=dict1.copy()
# print(dict2)


# dict2.clear()
# print(dict2)
# del dict2
# print(dict2)

# dub=dict.fromkeys(dict1,dict2)
# print(dub)

# x=dict1.get("Univarsity")
# print(x)

# y=dict1.items()
# print(y)

# y=dict1.keys()
# print(y)

# y=dict1.pop("Year")
# print(dict1)

# dict1.popitem()
# print(dict1)
# dict1.update({"branch":"CS"})
# print(dict1)

dict1.setdefault("R","p")
print(dict1)


# # dict13= dict1 | dict2
# # print(dict13)
# print(dict1)
# # dict1.update(dict2)
# # print(dict1)
# # dict1.update(list)
# # print(dict1)