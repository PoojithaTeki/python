import math
def jumpSearch(arr,x,n):

	step=math.sqrt(n)

	prev=0
	a=arr[int(min(step,n)-1)]
	print("a",a)
	while arr[int(min(step,n)-1)]<x:
		prev=step
		if prev>=n:
			return -1
	
	while arr[int(prev)]<x:	
		prev+=1
		#
		if prev==min(step,n):
			return -1
	if arr[int(prev)]==x:
		return prev
	return -1
arr=[1,3,5,22,54,77,87,95,343,567,888]
x=77
n=len(arr)
index=jumpSearch(arr,x,n)
print("number",x,"is at index","%.of",%index)