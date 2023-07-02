#cipher code 
#input:danger
#output:fcpigt
s=input("enter the string:")
n=0
for i in s:
	i=chr(ord(i)+2)
	print(i,end='')
print("\n")
while n<len(s):
	l=s[n]
	print(chr(ord(l)+2),end='')
	n+=1
