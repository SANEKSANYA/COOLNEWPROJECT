
import random

sym = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


length1 = int(input())


password = ""

for i in range(length1):
    letter = random.randint(0, len(sym)-1)
    password+=sym[letter]



print(password)


