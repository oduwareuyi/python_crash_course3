guest_list = ["Jenna", "rejoice", "My_love"]
message = "can I take you out for dinner tonight"
print(f"{guest_list[0].title()}, {message}\n")
print(f"{guest_list[1].title()}, {message}\n")
print(f"{guest_list[2].title()}, {message}\n")
not_active = guest_list.pop(0)
print(f"{not_active}, will not be coming\n")
guest_list.insert(0, "Angelina Jolie")
print(f"{guest_list[0]}, will be my new date\n")
print(guest_list)