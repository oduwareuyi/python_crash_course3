#7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

ten_multiple = int(input("Give me a number: "))

if ten_multiple % 10 == 0:
    print(f"The number {ten_multiple} is a multiple of 10")
else:
    print(f"The number {ten_multiple} is not a multiple of 10")