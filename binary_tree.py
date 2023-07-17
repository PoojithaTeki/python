#Binary tree

class BinaryTreeNode():
	def __init__(self,data):
		self.data=data
		self.leftChild=None
		self.rightChild=None
node1=BinaryTreeNode(11)
node2=BinaryTreeNode(22)
node3=BinaryTreeNode(33)
node4=BinaryTreeNode(44)
node5=BinaryTreeNode(55)
node6=BinaryTreeNode(66)
node7=BinaryTreeNode(77)

node1.leftChild=node2
node1.rightChild=node3
node2.leftChild=node4
node2.rightChild=node5
node3.leftChild=node6
node3.rightChild=node7

print("root node is:")
print(node1.data)
print("left child:")
print(node1.leftChild.data)
print("right child :")
print(node1.rightChild.data)

print("Node is :")
print(node2.data)
print("left child:")
print(node2.leftChild.data)
print("right child :")
print(node2.rightChild.data)


print("Node is :")
print(node3.data)
print("left child:")
print(node3.leftChild.data)
print("right child :")
print(node3.rightChild.data)

