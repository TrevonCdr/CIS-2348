# Trevon McKenzie
# 1880601

user_password = input()
character_key = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'}   # Creates a dictionary containing characters
strong_user_password = ''                                            # to be replaced as keys, and their replacements
                                                                     # as values
for character in user_password:                       # Outer for loop iterates through input password
   for symbol in character_key:                       # Inner for loop iterates through dictionary
      if character == symbol:                         # When and if a character matches a key in the dictionary,
         strong_user_password += character_key[symbol]# add the value of that key to the specified variable
         break
      else:
         continue
   else:                                              # If the inner loop concludes and there is
      strong_user_password += character               # no match, add the unchanged character to the
                                                      # specified variable
print(strong_user_password + 'q*s')