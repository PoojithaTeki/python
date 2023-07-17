def bubblesort(list):
#swap the elements to arramge in order 
	for i in range(len(list)-1,0,-1):  #i=6,5,4,3,2,1
	#y n minus and reverse bcs first pass last now dont touch that
		print("\ni values")
		print(i,end=' ')
		for j in range(i):  #if i=6 then j=0,1,2,3,4,5
			
			print(j,end=" ")
			if list[j]>list[j+1]:
				temp=list[j]
				list[j]=list[j+1]
				list[j+1]=temp
list=[2,-4,654,-325,5555,8,-4]
bubblesort(list)
print("\nsorted list:",list)