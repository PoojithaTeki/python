#deletion at end for double linked list 
class Node:
	def __init__(self,data):
		self.data=data
		self.prev=None
		self.next=None
class Dll:
	def __init__(self):
		self.head=None
	def delete_end(self):
		temp=self.head
		while temp.next :
			temp=temp.next
		temp.next.prev=None
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
obj.delete_end()
print("after deletion:")
obj.display()