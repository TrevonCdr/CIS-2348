# Trevon McKenzie
# 1880601

user_word = input()
word_no_spaces = user_word.replace(" ", "")     # replace all whitespace characters with
                                                # an empty string character
reversed_word = word_no_spaces[::-1]              # reverse the word or phrase using a slice

if word_no_spaces == reversed_word:                # check if the reversed word or phrase
   print(user_word, "is a palindrome")             # is equal to the original word
else:
   print(user_word, "is not a palindrome")

