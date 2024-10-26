#7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['Bánh mì', 'Cuban sandwich', 'Reuben sandwich', 'Chicken sandwich', 'Egg sandwich', 'jelly sandwich']

finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order}.")
    finished_sandwiches.append(order)

print("\nSandwiches that were made:\n")

for sandwich in finished_sandwiches:
    print(f'\t{sandwich}')
