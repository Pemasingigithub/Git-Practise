import random

u_number = int(input("Guess a number between 1 to 100:_"))
w_number = random.randint(1, 100)
i = 1
while u_number != w_number:
    if u_number < w_number:
        print("Too low number")
    else:
        print("Too high number")
    u_number = int(input("Guess again number:_"))
    i += 1
print(f"you win, and you guessed this number in {i} times!")
