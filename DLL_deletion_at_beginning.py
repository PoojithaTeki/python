#deletion at beginning for double linked list 
class Node:
	def __init__(self,data):
		self.data=data
		self.prev=None
		self.next=None
class Dll:
	def __init__(self):
		self.head=None
	def delete_begin(self):
		temp=self.head
		temp.next.prev=None
		self.head=temp.next
		temp.next=None
		
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
n3=Node(33)
n3.prev=n2
n2.next=n3
obj.display()
print("\n")
obj.delete_begin()
print("after deletion:")
obj.display()