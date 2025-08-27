import random
sec_number = random.randint(1,100)
attempt = 0
while True:
    guess = int(input("enter a number between 1 to 100: "))
    attempt +=1
    if guess < sec_number:
        print("too loww")
    elif guess > sec_number:
        print("too high")
    else:
        print(f"correct! you guessed it in {attempt} attempts")
        break