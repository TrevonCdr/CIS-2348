# Trevon McKenzie
# 1880601

integers = input()               # take list of integers as input from user
integer_list = integers.split()  # split list of integers into list

i = 0
for num in integer_list:         # convert string values in list to int values
    integer_list[i] = int(num)
    i += 1

integer_list_copy = integer_list[::]  # create copy of integer list

for num in integer_list:   # if integer is negative, remove it from the copy
    if num < 0:
        integer_list_copy.remove(num)


integer_list_copy.sort()          # output integer list
for integer in integer_list_copy:
    print(integer, '', end='')


