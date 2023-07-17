import random
arr=["rock","paper","scissor"]
c_choice=random.randint(0,2)
c_choice=arr[c_choice]
u_choice=input("enter ur choice:").lower()
if u_choice not in c_choice:
	print("Invalid choice")
if u_choice=="rock":
	if c_choice=="paper":
		print("comp won")
	elif c_choice=="scissors":
		print("user won")
	else:
		print("draw")
if u_choice=="scissors":
	if c_choice=="rock":
		print("comp won")
	elif c_choice=="paper":
		print("user won")
	else:
		print("draw")
if u_choice=="paper":
	if c_choice=="scissors":
		print("comp won")
	elif c_choice=="rock":
		print("user won")
	else:
		print("draw")