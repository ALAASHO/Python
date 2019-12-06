# Enjoy Coding
# For more Py Projects : https://github.com/ALAASHO/Python
# -----------------------------------------------------------------------

# Program to generate a random string of characters, length defined by user.
import random

# Define the list of characters to pull password from
all_Characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "n", "p", "q", "r", "s", 't',
                  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                  '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '<', '.', '>', '/',
                  '?']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '<', '.', '>', '/', '?']

print("Welcome to the Password Generator.")
length = int(input("How many characters do you want your password to be? "))

while length < 8:
    print("That password is not long enough to be secure.  Please make it at least 8 characters long.")
    length = int(input("How many characters do you want your password to be? "))
while length > 30:
    print("That password is too long to be accepted in most places.  Please make it less than 30 characters long.")
    length = int(input("How many characters do you want your password to be? "))
# Generate 1 of each value, then 26 other random values
p1 = random.choice(lower)
p2 = random.choice(upper)
p3 = random.choice(num)
p4 = random.choice(sym)
p5 = random.choice(all_Characters)
p6 = random.choice(all_Characters)
p7 = random.choice(all_Characters)
p8 = random.choice(all_Characters)
p9 = random.choice(all_Characters)
p10 = random.choice(all_Characters)
p11 = random.choice(all_Characters)
p12 = random.choice(all_Characters)
p13 = random.choice(all_Characters)
p14 = random.choice(all_Characters)
p15 = random.choice(all_Characters)
p16 = random.choice(all_Characters)
p17 = random.choice(all_Characters)
p18 = random.choice(all_Characters)
p19 = random.choice(all_Characters)
p20 = random.choice(all_Characters)
p21 = random.choice(all_Characters)
p22 = random.choice(all_Characters)
p23 = random.choice(all_Characters)
p24 = random.choice(all_Characters)
p25 = random.choice(all_Characters)
p26 = random.choice(all_Characters)
p27 = random.choice(all_Characters)
p28 = random.choice(all_Characters)
p29 = random.choice(all_Characters)
p30 = random.choice(all_Characters)
# Place all characters in a list, that list is the password
password = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23,
            p24, p25, p26, p27, p28, p29, p30]
# print(password)
random.shuffle(password)
# print(password)
# Print only the required number of characters
print("Your password is: ")
# sep='' for disabling the softspace feature.
print(*password[:length], sep='')
