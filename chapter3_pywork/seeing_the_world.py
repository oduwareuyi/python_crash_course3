locations = ["paris", "america", "dubai", "france", "china"]

print("Original Order:\t")
print(f"\t{locations}\n")

print("Temporary sorted list:")
print(f"\t{sorted(locations)}\n")

print("No permanent change:")
print(f"\t{locations}\n")

print("Temporary sorted reverse list:")
print(f"\t{sorted(locations, reverse = True)}\n")

print("No permanent change:")
print(f"\t{locations}\n")

#Reversing list
locations.reverse()
print("List in reverse order:")
print(f"\t{locations}\n")

print("Reversing list to original form:\n")
locations.reverse()
print(f"\t{locations}\n")

print("Permanent aphabetical arrangement:")
locations.sort()
print(f"\t{locations}\n")

print("Permanent reverse alphabetic list:")
locations.sort(reverse = True)
print(f"\t{locations}\n")