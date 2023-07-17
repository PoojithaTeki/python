#0,0,7,6,14,12...
#find 15th and 16th term
a=6
b=7
i=j=temp=1
l=[]
n=int(input("enter a number:"))
while temp<=n:
	if temp%2==0:
		l.append(a*(i-1))
		i+=1
	else:
		l.append(b*(j-1))
		j+=1
	temp+=1
print("{} th term is:{}".format(n,l[n-1]))