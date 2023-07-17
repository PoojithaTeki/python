#single linked list insertion at given position
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class SingleLinkedList:
	def __init__(self):
		self.head=None
	def insert_position(self,pos,data):
		np=Node(data)
		temp=self.head
		for i in range(pos-1):
			temp=temp.next
		np.next=temp.next
		temp.next=np
	def display(self):
		if self.head is None:
			print("Linked list is empty")
		else:
			temp=self.head
			while temp:
				print(temp.data,"==>",end="")
				temp=temp.next 
			
obj=SingleLinkedList()
n=Node(11)
obj.head=n
n1=Node(22)
n.next=n1
n2=Node(33)
n1.next=n2
n3=Node(44)
n2.next=n3
n4=Node(55)
n3.next=n4
print("before inserting")
obj.display()
print("")
print("after inserting")
obj.insert_position(3,6)
obj.display()