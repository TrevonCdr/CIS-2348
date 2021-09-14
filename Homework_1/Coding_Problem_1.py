# Trevon McKenzie
# 1880601

print("Birthday Calculator")

current_date = input("Please enter the current date (Month day year): ")
current_date = current_date.split()                                      # Split user input of current date into a list

birthday = input("Please enter your birthday (Month day year): ")
birthday = birthday.split()                                              # Split user input of birthday into a list

print('Current day\n'                  # Output user input of current date 
      f'Month: {current_date[0]}\n'       
      f'Day: {current_date[1]}\n'
      f'Year: {current_date[2]}')

print('Birthday\n'                     # Output user input of birthday
      f'Month: {birthday[0]}\n'
      f'Day: {birthday[1]}\n'
      f'Year: {birthday[2]}')

if current_date[0] < birthday[0]:                                              # Compare current month to birth month
    print("You are", int(current_date[2]) - int(birthday[2]), "years old")
elif current_date[0] > birthday[0]:
    print("You are", int(current_date[2]) - int(birthday[2]) - 1, "years old")
elif current_date[0] == birthday[0]:                                           # If both months are the same, then
    if current_date[1] > birthday[1]:                                          # compare current day to birth day
      print("You are", int(current_date[2]) - int(birthday[2]), "years old")
    elif current_date[1] < birthday[1]:
      print("You are", int(current_date[2]) - int(birthday[2]) - 1, "years old")
    else:
      print("Happy Birthday!")   # Current day and birthday match
else:
   print("You were never born")
