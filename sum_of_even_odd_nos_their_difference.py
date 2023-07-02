#sum of even and odd digits individual to the given number and difference to their sum 
#input: enter a number:4958
#output:sum of even no.s and odd no.s and their difference :2
#code:even digits sum:4+8=12 and odd digits sum :9+5=14 and absolute difference of their sum 14-12=2
n=int(input("enter a number:"))
r=se=so=0
while n!=0:
	r=n%10
	if r%2==0:
		se=se+r
	else:
		so=so+r
	n=n//10
print("sum of even no.s and odd no.s and their difference :",abs(so-se))