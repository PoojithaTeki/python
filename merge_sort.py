def merge_sort(unsorted_list):
	if len(unsorted_list)<=1:
		return unsorted_list
#find the middle point and divide it
	middle=len(unsorted_list)//2
	
	left_list=unsorted_list[:middle]
	right_list=unsorted_list[middle:]
	
	left_list=merge_sort(left_list)
	#print(left_list)
	right_list=merge_sort(right_list)
	return list(merge(left_list,right_list))
#merge thr sorted halves
def merge(left_half,right_half):
	res=[]
	while len(left_half)!=0 and len(right_half)!=0:
		if left_half[0]<right_half[0]:
			res.append(left_half[0])
			left_half.remove(left_half[0])
		else:
			res.append(right_half[0])
			right_half.remove(right_half[0])
	if len(left_half)==0:
		res=res+right_half
	else:
		res=res+left_half
	return res
unsorted_list=[432,-352,55,6,1,7,2,9]
print(merge_sort(unsorted_list))
unsorted_list=[34,7,1,8,3,-22,55]
print(merge_sort(unsorted_list))

	