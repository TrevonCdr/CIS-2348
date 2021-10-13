# Trevon McKenzie
# 1880601

import datetime

x = datetime.datetime.now()
current_date = datetime.datetime(int(x.strftime("%Y")), int(x.strftime("%m")), int(x.strftime("%d")))      # create date object containing current date in the format
                                                                                                           # (month-name day, year)
dates = []

months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
          "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

for x in range(6):                 # store user entered dates in list
   dates.append(input())

for date in dates:
      if date.find(',') != -1:    # check for comma                                   
         date = date.split()
      else:
         dates.remove(date)
         continue
      if date[0].isalpha() == True and len(date[2]) == 4:     # check that first element is alphabetic
         date[1] = date[1].replace(',', '')                   # remove comma from second element
         entered_date = datetime.datetime(int(date[2]), months[date[0]], int(date[1]))                 # create date object containing entered date
      else:
         dates.remove(date[0])
         dates.remove(date[1])
         dates.remove(date[2])
         continue
      if current_date > entered_date:                                    # compare current date and entered date
          print("{}/{}/{}".format(months[date[0]], date[1], date[2]))
