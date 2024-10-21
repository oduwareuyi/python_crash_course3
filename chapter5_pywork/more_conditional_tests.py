#• Tests for equality and inequality with strings
#• Tests using the lower() method
#• Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
#• Test whether an item is in a list
#• Test whether an item is not in a list

food = "marshed potato"
print(food == "marshed potato")
print(food != "marshed potato")

car = "BMW"
print(car.lower() == "bmw")
print(car.lower() != "bmw")

age = 18
print(age == 18)
print (age !=18)
print(age > 18)
print(age < 18)
print(age >= 18)
print(age <= 18)

print((food == "marshed potato") and (age == 18))
print((food == "marshed potato") or (age < 18))

beverages = ["milo", "dano", "ovaltine", "bournvita", "water"]

if "milo" in beverages:
    print(True)
    
print("bournvita" not in beverages)