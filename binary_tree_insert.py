#insertion in binary tree
class newNode:
	def __init__(self,data):
		self.key =data
		self.left=None
		self.right=None
#inorder traversal of binary tree
def inorder(temp):
	if (not temp):
		return
	inorder(temp.left)
	print(temp.key,end=" ")
	inorder(temp.right)
def insert(temp,key):
	if not temp:
		root=newNode(key)
		return
	q=[]
	q.append(temp)
	print(type(q))
	print(len(q))
	#do level order traversal until we find an empty place
	while len(q):
		print(len(q))
		temp=q[0]
		q.pop(0)
		if not temp.left:
			temp.left=newNode(key)
			break
		else:
			q.append(temp.left)
		if not temp.right:
			temp.right=newNode(key)
			break
		else:
			q.append(temp.right)
if __name__=='__main__':
	root=newNode(11)
	root.left=newNode(22)
	root.left.left=newNode(33)
	root.right=newNode(44)	
	root.right.left=newNode(55)
	root.right.right=newNode(66)	
	print("inorder traversal before insertion:",end=" ")
	inorder(root)
	key=35
	insert(root,key)
	print()
	print("inorder traversal after insertion:",end=" ")
	inorder(root)
	