import random

pass_len = int(input("Enter the length: "))

cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sim_letters = cap_letters.lower()
numbers = "0123456789"
african_shit = "()[]/\_?#$*"

upper, lower, digits, sym = True, True, True ,True

words = ""

if upper:
    words += cap_letters
if lower:
    words += sim_letters
if digits:
    words += numbers
if sym:
    words += african_shit

#length = 12
amount = 10

for x in range (amount):
    password = "".join(random.sample(words, pass_len))
    print(password)

