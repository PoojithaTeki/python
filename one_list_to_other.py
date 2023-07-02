#sending the elements from one list to another using a list
#output: [] [] [4,3,2,1]
def hanoi(n,a,b,c):
	if n>0:
		hanoi(n-1,a,b,c)
		if a:
			c.append(a.pop())
		hanoi(n-1,b,a,c)
a=[1,2,3,4]
b=[] 
c=[]
hanoi(len(a),a,b,c)
print(a,b,c)