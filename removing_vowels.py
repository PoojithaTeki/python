#printing only constants in given string by removing the vowels
#input: enter a string:happy
#output:hppy
s1=input("enter a string:")
s2=['a','e','i','o','u']
s=''
for i in range(len(s1)):
	if s1[i] not in s2:
		s=s+s1[i]
print(s)