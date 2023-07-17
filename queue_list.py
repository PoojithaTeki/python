#queue implementaation using list
queue=[]
def enqueue():
	ele=input("enter element:")
	queue.append(ele)
	print(ele," is added to queue")
def dequeue():
	if not queue:
		print("queue id empty")
	else:
		e=queue.pop(0)
		print("removed element:",e)
def display():
	print(queue)
while True:
	print("select a option 1.enqueue 2.dequeue 3.show 4.quit")
	choice=int(input())
	if choice==1:
		enqueue()
	elif choice==2:
		dequeue()
	elif choice==3:
		display()
	elif choice==4:
		break
	else:
		print("enter a number b/w 1 to 4")