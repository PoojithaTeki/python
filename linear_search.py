#the globals() method return a dictionary with all the global variables and symbols for the current program ,example: print(globals())
pos=-1
def search(list,n):
	i=0
	while i<len(list):	
		if list[i]==n:
			globals()['pos']=i
			return True
		i=i+1
	return False

list=[11,22,33,44,55]
n=55
if search(list,n):
	print("found it at position:",pos+1)
else:
	print("element is not found")