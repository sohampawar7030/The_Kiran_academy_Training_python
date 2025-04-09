set1={1,2,3,4,5,10,100,200}
set2={3,4,5,100,200}
#Union Method 
print("Use Union Method :",set1.union(set2))
print("Use Union Method :",set1 | set2)
#Update Method 
print("Use update Method :",set1.update(set2))
print("Use intersection Update Method :",set1.intersection_update(set2))

# Diffrence Method 

print("Use Diffrence  Method :",print(set1.difference(set2)))
print("Use Diffrence Method :",print(set1-set2))




