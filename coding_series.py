#n=5 then 5 16 8 4 2 1 
#n=6 then 6 3 10 5 16 8 4 2 1
#if odd (n*3)+1 ,if even n/2

def func(l):
	print(l,end=" ")
	if l%2==0:
		l=l//2	
		func(l)
	elif l==1:
		print()
	else:
		l=(l*3)+1
		func(l)
l=int(input("enter a number:"))
func(l)