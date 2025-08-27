numbers = [1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     # n = num % 2 == 0
#     # print(n)
#     if num % 2 == 0:
#         print(num)

# i  = 1
# while i < 60:
#     print(i)
#     i += 1
# print("i  is greater then 6")

# def add(a,b):
#     # a = int(input("Enter first number: "))
#     # b = int(input("Enter second number: "))
#     # c  = a + b
#     # print("the sum is ", c)
#     print( a + b)

# add(9,8)

def count_word(string):
    word = string.split()
    return len(word)
sen = "python is a popular programming language"
word_cout = count_word(sen)
print("number of words: ", word_cout)