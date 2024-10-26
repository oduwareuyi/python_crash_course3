#7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready

seating = int(input("How many people are in your dinner group? "))

if seating > 8:
    print("\nYou will have to wait for a table sir/ma")
else:
    print("\nYour table is ready sir/ma")