n=int(input("enter a len of str:"))
s=input("enter the code:")
p=r=c=0
if n!=len(s):
	print("len of code should be:",n)
else:
	while p<len(s):	  
		if int(s[p])==0:
			r=p+1
			break
		p+=1
	while r<len(s):
		if int(s[r])==1:
			c+=1
		elif int(s[r])==0:
			break
		r+=1
	print("count:",c)