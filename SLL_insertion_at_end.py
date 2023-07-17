#single linked list insertion at end
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class SingleLinkedList:
	def __init__(self):
		self.head=None
	def insert_end(self,data):
		ne=Node(data)
		temp=self.head
		while temp.next: 
			temp=temp.next
		temp.next=ne
	def display(self):
		if self.head is None:
			print("Linked list is empty")
		else:
			temp=self.head
			while temp:
				print(temp.data,"-->",end="")
				temp=temp.next 
			print("\b\b\b")
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
i=input("enter which number u want to insert at end:")
obj.insert_end(i)
obj.display()