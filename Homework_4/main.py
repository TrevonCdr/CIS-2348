# Trevon McKenzie
# 1880601

def partition(id_list, i, k):    # partition input user ids, find pivot
    middle = i + (k - i) // 2
    pivot = id_list[middle]
    h = k
    l = i
    finished = 'no'

    while finished != 'yes':                     # compare used ids to middle user id, increment l
        while id_list[l] < id_list[middle]:
            l += 1
        while pivot < id_list[h]:                # compare pivot to user id in upper partition, decrement h
            h -= 1
        if l >= h:                               # if l and h reached each other, terminate loop
            finished = 'yes'
        else:                                    # else, swap values and increment/decrement
            temp = id_list[l]
            id_list[l] = id_list[h]
            id_list[h] = temp
            l += 1
            h -= 1
    return h


def quicksort(id_list, i, k):
    global num_calls            # keep track of times quicksort is called
    num_calls += 1
    if i >= k:                  # check if already sorted
        return
    j = partition(id_list, i, k)
    quicksort(id_list, i, j)           # sort low partition and high partition
    quicksort(id_list, j + 1, k)
    return


num_calls = 0
id_list = []
user_input = input()

while user_input != '-1':       # accept and append user ids until user inputs -1
    id_list.append(user_input)
    user_input = input()

quicksort(id_list, 0, len(id_list) - 1)  # call function to sort ids
print(num_calls)

for id in id_list:   # output sorted id list
    print(id)
