#single linked list deletion at beginning (first node)
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class SingleLinkedList:
	def __init__(self):
		self.head=None
	def display(self):
		if self.head is None:
			print("Linked list is empty")
		else:
			temp=self.head
			while temp:
				print(temp.data,"==>",end="")
				temp=temp.next 
	def delete_position(self,pos):
		temp=self.head.next
		prev=self.head
		for i in range(1,pos-1):
			temp=temp.next
			prev=prev.next
		prev.next=temp.next
		temp.next=None
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
obj.display()
obj.delete_position(3)
print("\nafter deletion :")
obj.display()