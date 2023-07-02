n=int(input("enter no.of grams :"))
if n==0:
	print("estimated time is: 0min")
elif 0<n<=2000: #n>0 and n<=200 
	print("estimated time is: 25 min")
elif 2000<n<=4000:
	print("estimated time is: 35 min")
elif 4000<n<=7000:
	print("estimated time is: 45 min")
else:
	print("OVERFLOW")

#sir program
#elif n in range(2001,4001)
if n==0:
	print("estimated time is: 0min")
elif n in range(0,2001):
	print("estimated time is: 25 min")
elif n in range(2001,4001):
	print("estimated time is: 35 min")
elif n in range(4001,7001):
	print("estimated time is: 45 min")
else:
	print("OVERFLOW")


