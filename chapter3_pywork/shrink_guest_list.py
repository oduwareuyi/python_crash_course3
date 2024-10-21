print("I can only invite two people for dinner")
guest_list = ["Jenna", "rejoice", "My_love"]
not_active = guest_list.pop(0)
print(f"{not_active}, will not be coming\n")
guest_list.insert(0, "Angelina Jolie")
guest_list.insert(0, "Loveth")
guest_list.insert (1, "Happiness")
guest_list.append("Success")

guest0 = guest_list.pop()
guest1 = guest_list.pop()
guest2 = guest_list.pop()
guest3 = guest_list.pop()
message = "I am sorry I can't invite you for dinner"
print(f"{guest0}, {message}")
print(f"{guest1}, {message}")
print(f"{guest2}, {message}")
print(f"{guest3}, {message}")
print(f"{guest_list[0]}, you are still invited.")
print(f"{guest_list[1]}, you are still invited.")
del guest_list[0]
del guest_list[0]
print(guest_list)