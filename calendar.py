import calendar
y=int(input("enter the year:"))
m=1
cal=calendar.TextCalendar(calendar.SUNDAY)
i=1
while i<=12:
	cal.prmoth(y,i)
	i+=1