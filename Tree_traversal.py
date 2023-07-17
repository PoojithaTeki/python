#Tree traversal in 3 ways in-order,pre-order,post-order

class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.val=key
def Inorder(root):
	if root:
		#first recur on left child
		Inorder(root.left)
		#then print the data of node
		print(root.val,end=" ")
		#now recursion on right child
		Inorder(root.right)
def Preorder(root):
	if root:
		print(root.val,end=" ")
		Preorder(root.left)
		Preorder(root.right)
def Postorder(root):
	if root:
		Postorder(root.left)
		Postorder(root.right)
		print(root.val,end=" ")
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("pre-order:")
Preorder(root)
print("\nIn-order:")
Inorder(root)
print("\nPost-order:")
Postorder(root)



