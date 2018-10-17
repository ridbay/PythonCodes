from datetime import timedelta
name = input("What\'s your name: ")
print("Enter your DOB to know how long you have lived and how many days")

#accept input from user

year_input = int(input("Enter your year of birth e.g \'1990': "))
month_input = int(input("Enter your month of birth e.g \'4' for april: "))
day_input = int(input("Enter your day of birth e.g \'21':"))

date1 = datetime(year = year_input, month = month_input, day = day_input)
#Today's date and time
today_date = datetime.today()

#subtract today's date from the user' DOB
total = today_date - date1

#Next birthday date is(format to remove all date and time except the year(current year))
date3 = today_date.strftime("%Y")

#current year in str plus 1
nextyeardate = int(date3) + 1
#next DOB is current year plus user's month and day input
datenextyear = datetime(year = nextyeardate, month = month_input, day = day_input)
days_left = datenextyear - today_date
day_left = days_left.days
total_seconds_lived = total.total_seconds()
print("\n")
print("Hi", name)
print("You have lived ",total.days,"days, which equals to", total_seconds_lived,"seconds on earth")
print("You have",day_left," days to your next birthday and your next birthday is",datenextyear.strftime("%b/%d/%Y"))
