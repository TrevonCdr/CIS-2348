# Trevon McKenzie
# 1880601

peoples_age = {}        # create an empty dictionary

info = input()
while info != '-1':       # prompt user input and check that it is not -1
    try:
        split_info = info.split()                            # try block of code that splits user input and
        split_info[1] = int(split_info[1])                   # converts the second element to an integer and adds
        peoples_age[split_info[0]] = split_info[1] + 1       # 1
        info = input()
    except ValueError:                                       # if second element cannot be converted to an integer
        peoples_age[split_info[0]] = 0                       # assign a value of 0
        info = input()

for name in peoples_age:               # output names with updated ages
    print(name, peoples_age[name])
