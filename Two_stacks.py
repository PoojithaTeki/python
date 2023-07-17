#create two stack
#define size of both stacks as 5
#if the input is even number it has to pushed in stack 1 and other inputs has to be pushed into stack2
#options: push/pop/display_stack/Quit

stack1=[]
stack2=[]
def push():
	for i in range(5):
		ele=int(input("enter element:"))
		if ele%2==0:
			stack1.append(ele)
		else:
			stack2.append(ele)
def pop():
	s=int(input("1 or 2:"))
	if not stack1 and stack2:
		print("stack is empty")
	elif s==1:
		e1=stack1.pop()
		print("removed element from stack1:",e1)
		print(stack1)
	else:
		e2=stack2.pop()
		print("removed element from stack2:",e2)
		print(stack2)
def display():
	c=int(input("1 or 2:"))
	if c==1:
		print(stack1)
	else:
		print(stack2)
while True:
	print("select the operation 1.push,2.pop,3.show and 4.quit")
	ch=int(input())
	if ch==1:
		push()
	elif ch==2:
		pop()
	elif ch==3:
		display()
	elif ch==4:
		break
	else:
		print("select the correction operation")

		