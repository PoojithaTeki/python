#cube of a first 10 numbers 
cube=[]
for i in range (0,11):
	cube.append(i**3)
print(cube)

#another method 
c=[j**3 for j in range(11)];print(c)