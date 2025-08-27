# set = {'ifra','ifra','usman','mubashar'}
# sets = {'ifra',}
# setss = {'ifra'}
# print(set)
# print(len(set))
# print(type(set))
# print(type(sets))
# print(type(setss))

# s = {1,2}
# s2 = [1, 2, 3, 4, 5]
# s3 = (1, 2, 3, 5)
# s.add(3)
# s.update(s2) #list with sets 
# s.update(s3)#tuple with sets
# print(s)

# s2.remove(3)
# print(s2)

# s.discard(3)#error nii dy ga
# s.remove(3)#error dy ga agar 3 nahi hai
# print(s)

a = {1, 2, 3}
b = {1, 2, 3}

# b = {3, 4, 5}
# b = {1,3}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(b.difference(a))
# print(a.issubset(b))  # Check if a is a subset of b
# print(b.issubset(a))  # Check if b is a subset of a means part of a
print(a.issuperset(b))  # Check if a is a superset of b
#Check karta hai ke kya pehla set mein doosre set ki sari values hain