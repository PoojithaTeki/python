#login program using dictionary

login={"username":"p.8903","password":"qwerty"}
s1=input("enter the username:")
s2=input("enter the password:")
if s1!=login["username"]:
	print("invalid username")
elif s2!=login["password"]:
	print("wrong password")
else:
	print("login successful")