import random

for i in range(0, 1):
    randomn = random.randint(1, 20)
#    print(randomn)

for ii in range(1, 8):
    guessedn = int(input("Enter a number between 0 and 20 :"))
    if guessedn == randomn:
        print("Congratulation, your guess is true :=)")
        break
    elif guessedn > randomn:
        print("Wrong, You have been high from the right number! Try again.. This is your", ii, "attempt.")
    elif guessedn < randomn:
        print("Wrong, You have been low from the right number! Try again.. This is your", ii, "attempt.")
