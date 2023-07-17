'''l=[-3,4,6,-6,-9,5,3,-4]
max_so_far=0
max_ending_here=0
for i in range(0,len(l)):
	max_ending_here=max_ending_here+i
	if max_ending_here<0:
		max_ending_here=0
	if max_ending_here>max_so_far:
		max_so_far=max_ending_here
print()'''
def max_subarr_sum(arr,arr_size):
	maxTillNow=arr[0]
	maxEnding=0
	for n in range(0,arr_size):
		maxEnding=maxEnding+arr[n]
		if maxEnding<0:
			maxEnding=0
		elif maxTillNow< maxEnding:
			maxTillNow=maxEnding
	return maxTillNow
arr=list(map(int,input()))
print("max subarray sum:",max_subarr_sum(arr,len(arr)))