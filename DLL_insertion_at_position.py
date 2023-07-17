#insertion at given position for double linked list 
class Node:
	def __init__(self,data):
		self.data=data
		self.prev=None
		self.next=None
class Dll:
	def __init__(self):
		self.head=None
	def insert_pos(self,pos):
		n=Node(99)
		temp=self.head
		for i in range (1,pos-1):
			temp=temp.next
		n.prev=temp
		n.next=temp.next
		temp.next.prev=n
		temp.next=n
		
	def display(self):
		if self.head is None:
			print("empty")
		else:
			temp=self.head
			while temp:
				print(temp.data,"<-->",end=" ")
				temp=temp.next
obj=Dll()
n1=Node(11)
obj.head=n1
n2=Node(22)
n2.prev=n1
n1.next=n2
obj.display()
print("\n")
obj.insert_pos(3)
print("after insertion:")
obj.display()