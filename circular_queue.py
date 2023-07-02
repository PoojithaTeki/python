#circular queue 
#insert: rear=rear+1
#delete: front=front+1

class CircularQueue():
	def __init__(self,size):
		self.size=size
		#can use self.queue=[None]*size
		self.queue=[None for i in range(size)]
		self.front=self.rear=-1
	def enqueue(self,data):
		#condition if queue is full
		if ((self.rear+1) %self.size== self.front): #size 6 index from 0
			print("Queue is full\n")	
		#condition for empty queue
		elif (self.front== -1):
			self.front=0
			self.rear=0
			self.queue[self.rear]=data
			#always add ele at tail 
		else:
			#next position of rear	
			self.rear=(self.rear+1) %self.size
			self.queue[self.rear]=data
	def dequeue(self):
		if (self.front==-1):  #condition for empty
			print("Queue is empty\n")
		#condition for only one element
		elif (self.front == self.rear):
			temp=self.queue[self.front]
			self.front=-1
			self.rear=-1
			return temp
		else:
			temp=self.queue[self.front]
			self.front=(self.front+1) %self.size
			return temp
	def display(self):
		#condition for empty queue
		if (self.front==-1):
			print("Queue is empty\n")
		elif (self.rear>=self.front):
			print("elements in circular queue:",end=" ")
			for i in range (self.front,self.rear+1):
				print(self.queue[i],end=" ")
			print("")
		else:
			print("elements in circular queuer:",end=" ")
			for i in range(self.front,self.size):
				print(self.queue[i],end=' ')
			for i in range(0,self.rear+1):
				print(self.queue[i],end=' ')
			print(" ")
		if ((self.rear+1) %self.size==self.front):
			print("Queue is full")
ob=CircularQueue(5)
ob.enqueue(11)
ob.enqueue(22)
ob.enqueue(-33)
ob.enqueue(44)
ob.display()
print("Deleted value=",ob.dequeue())
print("Deleted value=",ob.dequeue())
ob.display()
ob.enqueue(55)
ob.enqueue(66)
ob.enqueue(77)
ob.display()



				
