# Trevon McKenzie
# 1880601

words = input()            # accept words from user
words_list = words.split() # make list of words

for word in words_list:             # count the number of times the word is in the list
    count = words_list.count(word)
    print(word, count)              # output the word along with count

