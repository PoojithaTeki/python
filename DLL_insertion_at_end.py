#insertion at end for double linked list 
class Node:
	def __init__(self,data):
		self.data=data
		self.previous=None
		self.next=None
class Dll:
	def __init(self):
		self.head=None
	def insert_end(self):
		n=Node(99)
		temp=self.head
		while temp.next is not None:
			temp=temp.next
		temp.next=n
		n.previous=temp
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
obj.insert_end()
print("after insertion:")
obj.display()