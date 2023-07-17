#accessing private variable __
class encap:
	__a=33
	print("in class:",__a)
	def fun(self):
		print("inside the method in class:",self.__a)
obj=encap()
obj.fun()
print(obj.__a) #will throw the error i.e attribute error