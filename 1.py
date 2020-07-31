days_month=[31,28,31,30,31,30,31,31,30,31,30,31]
days_month_leap=[31,29,31,30,31,30,31,31,30,31,30,31]

day=2
count=0

for year in range(1901,2001):
	months=days_month
	if year%4==0:
		months=days_month_leap
	if year % 100 == 0:
		months= days_month
	if year %400 ==0:
		months= days_month_leap
	
	yearday=0

	for month in months:
		for monthday in range(month):
			if day%7==0 and monthday==0: count+=1
			day+=1

print(count)
