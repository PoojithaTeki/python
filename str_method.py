x='pooji'
y='789'
z='      shivayya rama   '
a=' rp rp rp '
b=' PooJi'
c=' shivayya rama krishna '
d='3pooji'
e='r a'
p=0
print(max(x)) #max in letter
print(min(x))
print(max(y))
print(min(y)) #min in no.s
print(z.lstrip()) #removes the spaces
print(a.replace('p','c')) #replaces p with c
print(b.swapcase()) #upper becomes lower viceverse
print(c.split(',')) #splits the spaces with ',' even other than ',' is given it prints ','
print('-'.join(c)) #spaces are filled with '-'
print(list(enumerate(c))) #gives the index and letter in list 
print(d.isalnum()) #checks if the complete string is alpha numeric
print(y.isdigit()) # '' if full string is numeric then TRUE otherwise false
print(y.isalpha())
print(x)
print(x[1:5])
print(x[:4])
print(x[:])
print(x[2:])
print(x[:-3])
print(x[::-1])
print(x[::3])
print(ord('='))
print(chr(69))
if e in c :
	print("found")
else:
	print("not found")
for i in x:
	print(i,end=" ")
while p<len(x):
	print(x[p],end=" ")
	p+=1
	