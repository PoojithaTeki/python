#converting binary number to decimal number
bn=int(input("enter a binary number:"))
dn=r=i=0
while bn!=0:
	r=bn%10
	dn=dn+r*(2**i)
	bn=bn//10
	i+=1
print("decimal number is:",dn)