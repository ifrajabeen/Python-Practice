m = int(input("Enter the number of matches: "))
month = int(input("Enter the month (1-12): "))
match m:
    case 1 | 2 | 3 | 4 | 5 if month == 1:
        print("You have selected match ",m+1)
    case 1 | 2 | 3 | 4 | 5 if month == 2:
        print("You have selected match ",m)
    case _:
        print("Invalid match number")  # Default case if no other cases match