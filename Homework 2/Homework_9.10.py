# Trevon McKenzie
# 1880601

import csv

entered_file = input()

my_file = open(entered_file, 'r')                        # open file for reading
reader = csv.reader(my_file, delimiter = ',')    # read csv file using commas as separators
tracker = {}                                     # tracker counts repeated words
for line in reader:                              # iterate through lists of list to count the number of
   for word in line:                             # times a word appears
      if word in tracker:
         tracker[word] = tracker[word] + 1
      else:
         tracker[word] = 1
my_file.close()

for phrase in tracker:                            # output dictionary keys and values
   print(phrase, tracker[phrase])



