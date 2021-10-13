# Trevon McKenzie
# 1880601

def exact_change(user_total):   # define function exact_change to calculate amount of change
    dollar_change = 0           # with the fewest amount of coins
    quarter_change = 0
    dime_change = 0
    nickel_change = 0
    penny_change = 0

    if user_total / 100 >= 1:                            # multiple if else statements check if user_total
        dollar_change = user_total // 100                # is greater than than a dollar, quarter, dime, nickel,
        user_total = user_total - (dollar_change * 100)  # or penny. If so, then user_total is assigned the proper
    if user_total / 25 >= 1:                             # number of coins
        quarter_change = user_total // 25
        user_total = user_total - (quarter_change * 25)
    if user_total / 10 >= 1:
        dime_change = user_total // 10
        user_total = user_total - (dime_change * 10)
    if user_total / 5 >= 1:
        nickel_change = user_total // 5
        user_total = user_total - (nickel_change * 5)
    if user_total / 1 >= 1:
        penny_change = user_total // 1
    return dollar_change, quarter_change, dime_change, nickel_change, penny_change

if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)  # unpacks tuple containing
                                                                                              # containing coin values
    num_change = [num_dollars, num_quarters, num_dimes, num_nickels, num_pennies]
    name_of_coin = ['dollar', 'quarter', 'dime', 'nickel', 'penny']
    i = 0

    if input_val == 0:
       print("no change")

    for x in num_change:
       if x == 0:
          i += 1                                 # iterates through num_change list and determines
          continue                               # whether the number of coins is greater than 1.
       if x > 1 and name_of_coin[i] != 'penny':  # If so, then the plural form is employed
          print(x, name_of_coin[i] + 's')
       elif x > 1 and name_of_coin[i] == 'penny':
          print(x, 'pennies')
       else:
          print(x, name_of_coin[i])
       i += 1
