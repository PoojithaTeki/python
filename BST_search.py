#searching a element in binary search tree
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
def search(root,key):
	if root is None or root.val==key:
		return root
	elif root.val<key:
		return search(root.right,key)
	elif root.val>key:
		return search(root.left,key)
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

r=search(r,80)
r=search(r,60)
r=search(r,40)
r=search(r,20)
r=search(r,30)
inorder(r)
	
	
	