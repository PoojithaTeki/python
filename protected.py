#protected _
class encap:
	_a=99
	b=77
	def med(self):
		_c=88
		print("encap function acessing protected")
		print(self._a+44)
obj=encap()
print(obj._a)
obj.med()
print(obj.b)
