#nth term of fibonacci f(n)=f(n-1)+f(n-2)
def fib(n):
	if n==1:
		return 0 
	elif n==2:
		return 1
	else:
		return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))