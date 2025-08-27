# print("enter any sentence")
# sen = input()
# print(sen.upper())


# a = "hello world how are you"
# print(a.replace(" ", "_"))
 #first old and separated it with , and then new value
# string.replace(oldvalue, newvalue, count)

# string = " Python is fun! "
# print(string.strip())
#use to remove spaces from the beginning and end of the string

# counting = "banana and apple"
# print(counting.count("a"))

# string = "name-age-country"
# print(string.split("-"))

# n = int(input("enter the number : "))
# if n % 2 != 0:
#     print("weird odd")
# elif n % 2 == 0  and 2 <= n <= 5:
#     print("Not weird range 2 to 5")
# elif n % 2 == 0 and 6<= n <=20:
#     print("weird even")
# elif n % 2 == 0 and n > 20:
#     print("not weird n > 20")
# else:
#     print("invalid case")


# Print numbers from 1 to n. For multiples of 3, print "Fizz" instead of the number. For multiples of 5, print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz".
# user = int(input("enter a number: "))
# for i  in range(1,user + 1):
#     if i % 3 == 0  and i% 5 == 0: 
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# Ask the user for a number n, and print all prime numbers from 2 to n.

# number = int(input("enter a number "))
# for num in range(2, number + 1):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)


# number = int(input("enter a number :"))
# for num in range(2,number + 1):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#          print(num)


# Take a number n and compute its factorial (e.g., 5! = 5×4×3×2×1 = 120) using a for loop

# n = int(input("enter a number for factorial: "))
# f = 1 
# for i in range(n):
#     f = f * (i +1)
# print(f"The factorial of {n} is {f}")


# Ask the user to enter a string and count the number of vowels and consonants in it.

# string = input("enter a string: ")
# for i in string:
#     if i in "aeious" or i in "AEIOUS":
#       print(f"{i} is a vowel")
#     elif i.isalpha():
#       print(f"{i} is a consonant")
#     else:
#       print(f"{i} is not a letter")

# Write a program that takes a list of numbers and returns the sum of all even numbers in the list.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_of_evens = 0
# for n in numbers:
#     if n%2 == 0:
#         sum_of_evens += n
#         print(f"The sum of even numbers in the list is {sum_of_evens}")


