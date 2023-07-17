#fibonacci series nth term with dynamic programming storing the values
def fib(n,l):
	if n==0:
		return 0
	elif n==1:
		return 1
	elif l[n]!=-1:
		return l[n]
	else:
		l[n]=fib(n-1,l)+fib(n-2,l)
		return l[n]
n=int(input("Enter a num:"))
l=[-1]*10
print(fib(n,l))