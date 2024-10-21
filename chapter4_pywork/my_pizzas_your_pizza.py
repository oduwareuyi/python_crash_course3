pizzas = ["Margherita Pizza", "Pepperoni Pizza", "Hawaiian Pizza"]
friend_pizzas = pizzas[:]
pizzas.append("Cheese Pizza")
friend_pizzas.append("Veggie Pizza")
print("My favourite pizzas are:")
for pizza in pizzas:
  print(pizza)
print("\n")

print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
  print(pizza)