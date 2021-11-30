# Trevon McKenzie
# 1880601

def selection_sort_descend_trace(integer_list):    # sort list in descending order
    for i in range(len(integer_list) - 1):
        smallest_index = i
        for j in range(i + 1, len(integer_list)):                  # inner loop to find index of smallest number
            if integer_list[j] > integer_list[smallest_index]:
                smallest_index = j
        temporary = integer_list[i]
        integer_list[i] = integer_list[smallest_index]      # swap numbers
        integer_list[smallest_index] = temporary
        for i in integer_list:      # output changed list after each iteration of outer loop
            print(i, '', end='')
        print()

integers = input()
integer_list = integers.split()    # split list of integers

for i in range(len(integer_list)):       # convert string values to integer values
    integer_list[i] = int(integer_list[i])

selection_sort_descend_trace(integer_list)

