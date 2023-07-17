def partition(arr,low,high):
	i=low-1
	pivot=arr[high]
	for j in range(low,high):
		#if current ele is smaller
		if arr[j]<=pivot:
			i=i+1
			arr[i],arr[j]=arr[j],arr[i]
	arr[i+1],arr[high]=arr[high],arr[i+1]
	return(i+1)
#sort
def quickSort(arr,low,high):
	if low<high:
		#index
		pi=partition(arr,low,high)
		#sort the partitions
		quickSort(arr,low,pi-1)
		quickSort(arr,pi+1,high)
arr=[3,45,6,7,1,-4,2]
n=len(arr)
quickSort(arr,0,n-1)
print("sorted arr:")
for i in range(n):
	print(arr[i],end=" ")