# this program will use a varible to dtermine what stage you are in life

age = 35

if age < 2:
    stage = "baby"
elif age < 4:
    stage = "toddler"
elif age < 13:
    stage = "kid"
elif age < 20:
    stage = "teen"
elif age < 65:
    stage = "adult"
elif age >= 65:
    stage = "elder"

print (f"You are a {stage}.")