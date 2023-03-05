import datetime
import random
print("Insert 2 dates in the format YYYY-MM-DD")

date1 = input("Insert the first date: ")
date2 = input("Insert the second date: ")

date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

difference = date2 - date1
increment = random.randint(0, difference.days)

finalDate = date1 + datetime.timedelta(days=increment)

print("The random date is: " + str(finalDate.strftime("%Y-%m-%d")))