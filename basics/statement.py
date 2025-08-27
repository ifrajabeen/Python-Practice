# a=3
# b=34
# if(a>b):
#     print("a is greater then b")
# elif(a==b):
#     print("a is equal to b")
# else:
#     print("b is greater then a")

x=200
g=23
c=500
if(x<g or g>c):
    print("At least one of the conditions is True")
elif(x>g and g<c):
    print("both of the conditions are true")
elif(not x<g):
    print("x is not less than g")
else:
    print(c)