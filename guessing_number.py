#Guessing the number
import random
n=random.randrange(1,100)
guess=int(input("enter a number:"))
while n!=guess:
	if guess>n:
		print("number is too high!!")
		guess=int(input("enter a number again:"))
	elif guess<n:
		print("number is too low!!")
		guess=int(input("enter a number again:"))
	else:
		break
print("you guessed it right")