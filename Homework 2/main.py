# Trevon McKenzie
# 1880601

import datetime

x = datetime.datetime.now()
current_date = datetime.datetime(int(x.strftime("%Y")), int(x.strftime("%m")), int(x.strftime("%d"))) # creates date
                                                                                                      # object containing
months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,        # current day
          "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

my_file = open('inputDates.txt', 'r')
my_second_file = open('parsedDates.txt', 'w')

for line in my_file:                                      # iterate over lines in file, test conditions on dates,
      if line.find(',') != -1:                            # and if conditions are passed, create date object containing
         line = line.split()                              # input date
      else:
         continue
      if line[0].isalpha() == True and len(line[2]) == 4:
         line[1] = line[1].replace(',', '')
         entered_date = datetime.datetime(int(line[2]), months[line[0]], int(line[1]))
      else:
         continue
      if current_date > entered_date:                    # compare current date with input date
          my_second_file.write("{}/{}/{}\n".format(months[line[0]], line[1], line[2]))  # output to parsedDates.txt

my_second_file.close()