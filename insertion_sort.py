def insertionsort(arr):
	#traverse through 1 to len(arr)
	for i in range(1,len(arr)):
		key=arr[i]
		#move eles of arr[0..i-1] that re greater than key to one position ahead of their current pos
		j=i-1
		while j>=0 and key<arr[j]:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key
arr=[12,33,6,2,45,9]
insertionsort(arr)
print("sorted array is :")
for i in range(len(arr)):
	print("%d"%arr[i])