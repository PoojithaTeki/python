b=[]
def selectionsort(a):
	k=0
	for i in range (0,len(a)):
		k=min(a)
		b.append(k)
		a.remove(k)
a=[3,66,2,54,97]
selectionsort(a)
print(b)