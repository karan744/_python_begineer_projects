import random
a= int(input("Enter the lower value of the numbers to be guessed: "))
b= int(input("Enter the upper value of the numbers to be guessed: "))
c=random.randint(a,b)
print("NUMBER GUESSING GAME")
choice=int(input(f"Game: Guess a number from {a} to {b}:: "))
while choice!=c:
    choice=int(input(f"Game: Guess the number again!!:: "))

print(f"Game: The number is correct!! Ans:{c}")
