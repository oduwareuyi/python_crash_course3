numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number % 10 == 1 and number != 11:
        print(f"{number}st")
    elif number % 10 == 2 and number != 12:
        print(f"{number}nd")
    elif number % 10 == 3 and number != 13:
        print(f"{number}rd")
    else:
        print(f"{number}th")