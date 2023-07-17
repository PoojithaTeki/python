n=int(input("enter a number:"))
sum=0.0
for i in range(1,n+1,1):
	sum=sum+(i/i+1)
print("sum of inverse of number :",sum)