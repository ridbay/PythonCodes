from datetime import datetime
date1 = datetime(year = 1989, month = 4, day = 21)
date2 = datetime.today()
total = date2 - date1
print(total)
total2 = total.total_seconds()
print(total2)
