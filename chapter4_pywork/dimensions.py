dimensions = (200, 50)

print(dimensions[0])

print(dimensions[1])
my_t = (3,)
print(my_t[0])
print("Using for loop:")
for dimension in dimensions:
    print(dimension)
 
dimensions = (400, 100)

print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#Trying with strings
names = ("James", "Author")

for name in names:
    print(name)