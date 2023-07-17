#insertion and creation of BST

class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.val=key
def insert(root,key):
	if root is None:
		return Node(key)
	else:
		if root.val==key:
			return root
		elif root.val>key:
			root.left=insert(root.left,key)
		else:
			root.right=insert(root.right,key)
	return root
#in order traversal
def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)
#       50
#    /      \
#  30       70
# /  \     /  \
#20  40   60  80
r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)
inorder(r)
	