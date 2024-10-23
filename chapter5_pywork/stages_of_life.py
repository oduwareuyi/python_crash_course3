age = 65

if age < 2:
    stage = "baby"
elif age >2 and age <4:
    stage ="Toddler"
elif age > 4 and age < 13:
    stage = "kid"
elif age > 13 and age < 20:
    stage = "teenager"
elif age > 20 and age < 65:
    stage = "adult"
elif age >= 65:
    stage = "elder"

if stage[0] == "a":
    print(f"You are an {stage}")
else:
    print(f"You are a {stage}")