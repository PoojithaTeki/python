import random
arr=["rock","paper","scissor"]
c_choice=random.randint(0,2)
c_choice=arr[c_choice]
u_choice=input("enter ur choice:").lower()
if u_choice not in c_choice:
	print("Invalid choice")
elif c_choice == "rock" and u_choice=="scissor":
	print("computer won") 
elif c_choice == "paper" and u_choice=="rock":
	print("computer won") 
elif c_choice == "scissor" and u_choice=="paper":
	print("computer won")
elif c_choice==u_choice:
	print("Draw match")
else:
	print("you won")
