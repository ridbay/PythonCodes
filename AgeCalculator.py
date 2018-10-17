from datetime import timedelta
name = input("What\'s your name: ")
print("Enter your DOB to know how long you have lived")

#accept input from user

year_input = int(input("Enter your year of birth e.g \'1990': "))
month_input = int(input("Enter your month of birth e.g \'4' for april: "))
day_input = int(input("Enter your day of birth e.g \'21' "))
date1 = datetime(year = year_input, month = month_input, day = day_input)
date2 = datetime.today()
total = date2 - date1
print("\n")
print("Hi", name)
print("You have lived ",total)
total2 = total.total_seconds()
print("\n")
print("and \n\n You have lived ", total2,"seconds")
