# import calendar
# import datetime
from datetime import date

print('*'  * 10)
print('Welcome from Krishna :\) ')
print('*'  * 10)
print(10 * 3)
#print(calendar.month(2022, 9))
#datetime.date()
todays_date = date.today()
print (todays_date)
print(todays_date.month)
#extract_date = format(todays_date,string)
#extract_date = extract_date(-5)
#print(extract_date)
if todays_date.month>5:
    print("Time to chill ")
else:
    print(f"Wait or enjoy the mangoes as the month is {todays_date.month}")

