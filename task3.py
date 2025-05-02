import random

ans = random.randint(1,10)
if ans > 5:
    print(f"You won. Number was {ans}")
else:
    print("You lost")