l=[3,-1,5,6,-3,-10]
l1=[0]*10
i=0
while i<len(l):
	l1[i+1]=(l1[i]+l[i])
	i+=1
i=0
print(l1)
while i<len(l1):
	if max(l1)==l1[i]:
		j=i
		break
	i+=1
print(l[:j]) 

	