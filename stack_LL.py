#stack implementation of Linked list
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class Stack:
	def __init__(self):
		self.head=None
	def is_empty(self):
		if self.head==None:
			return True
		else:
			return False
	def push(self,data):
		if self.head==None:
			self.head=Node(data)
		else:
			new_node=Node(data)
			new_node.next=self.head
			self.head=new_node
	def pop(self):
		if self.is_empty():
			return None
		else:
			popped_node=self.head
			self.head=self.head.next
			popped_node.next=None
			return popped_node.data
	def peek(self):
		if self.is_empty():
			return None
		else:
			return self.head.data
	def display(self):
		t=self.head
		if self.is_empty():
			print("stack is underflow")
		else:
			while t!=None:
				print(t.data,end="")
				t=t.next
				if t!=None:
					print("-->",end="")
			return
if __name__=="__main__":
	s=Stack()
	s.push(11)
	s.push(22)
	s.push(33)
	s.push(44)
	s.display()
	print("")
	print("peek",s.peek())
	s.pop()
	s.pop()
	s.display()
	print("")
	print("peek",s.peek())