#deletion operation in binary search tree

class Node:
	def __init__(self,key):
		self.key=key
		self.left=None
		self.right=None
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key)
		inorder(root.right)
def insert(node,key):
	if node is None:
		return Node(key)
	if key<node.key:
		node.left=insert(node.left,key)
	else:
		node.right=insert(node.right,key)
	return node
#given a non empty binary search tree ,return the node with minimum key value found in that tree
#note that the entire tree does not need to be searched
def minValueNode(node):
	current=node       #right subtree
	#
	while (current.left is not None):
		current=current.left
	return current

def deleteNode(root,key):
	#Base case
	if root is None:
		return root
	#key<root, it lies in left subtree
	if key<root.key:
		root.left=deleteNode(root.left,key)
	elif key>root.key:
		root.right=deleteNode(root.right,key)
	#if key is same as root's key,then this is to be deleted
	else:
		#Node with only one child or no child
		if root.left is None:
			temp=root.right
			root=None
			return temp
		elif root.right is None:
			temp=root.left
			root=None
			return temp
		#node with two children : get the inorder successor
		#smallest value in right subtree
		temp=minValueNode(root.right)
		#
		root.key=temp.key
		#
		root.right=deleteNode(root.right,temp.key)
	return root
#let us create the following BST
#       50
#    /      \
#  30       70
# /  \     /  \
#20  40   60  80
root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)
print("inorder traversal of the given tree:")
inorder(root)
print("\n delete 20")
root=deleteNode(root,20)
print("\nInorder traversal of modified tree:")
inorder(root)
print("\n delete 30")
root=deleteNode(root,30)
print("\nInorder traversal of modified tree:")
inorder(root)
print("\n delete 50")
root=deleteNode(root,50)
print("\nInorder traversal of modified tree:")
inorder(root)


