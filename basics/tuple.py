# tuple = ('ali',"fahad","hamza")
# tuple1 = ('ali',)
# str = ('ali')
# print(tuple)
# print(type(tuple1))
# print(type(str))
# print(type(tuple))

# t = (1,2,23,4,6,23,45,2,23,56)
# print(t.count(23))
# print(t.index(23))  # Returns the first index of the value 23

#Immutable:
#Faster than lists
#Used for fixed data: Jaise (latitude, longitude), days of week, etc.

#joining two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#repeat a tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)