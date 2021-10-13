# Trevon McKenzie
# 1880601

import datetime

x = datetime.datetime.now()
current_date = datetime.datetime(int(x.strftime("%Y")), int(x.strftime("%m")), int(x.strftime("%d")))

dates = []

months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
          "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

for x in range(6):
   dates.append(input())

for date in dates:
      if date.find(',') != -1:
         date = date.split()
      else:
         dates.remove(date)
         continue
      if date[0].isalpha() == True and len(date[2]) == 4:
         date[1] = date[1].replace(',', '')
         entered_date = datetime.datetime(int(date[2]), months[date[0]], int(date[1]))
      else:
         dates.remove(date[0])
         dates.remove(date[1])
         dates.remove(date[2])
         continue
      if current_date > entered_date:
          print("{}/{}/{}".format(months[date[0]], date[1], date[2]))
