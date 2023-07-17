#Stack is LIFO-last in first out
stack=[]
def push():
	ele=int(input("enter a element:"))
	stack.append(ele)
	print(stack)
def pop_ele():
	if not stack:
		print("stack is empty")
	else:
		e=stack.pop()
		print("removed element:",e)
		print(stack)
while True:
	print("select one option 1.push, 2.pop ,3.Quit:")
	choice=int(input())
	if choice==1:
		push()
	elif choice==2:
		pop_ele()
	elif choice==3:
		break
	else:
		print("invalid choice, select only 1,2,3")
