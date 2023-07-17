#creation of single linked list
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class Sll:
	def __init__(self):
		self.head=None
	def display(self):
		if self.head is None:
			print('Linked list is empty')
		else:
			temp=self.head
			while(temp):
				print(temp.data,'-->',end="")
				temp=temp.next
obj=Sll()
n1=Node(100)
obj.head=n1
n2=Node(200)
obj.head.next=n2
n3=Node(300)
n2.next=n3
obj.display()