# Trevon McKenzie
# 1880601

def fat_burning_heart_rate(age):      # function that calculates the fat burning heart rate of an adult
    heart_rate = 0.70 * (220 - age)
    return heart_rate


def get_age():                       # function that accepts the user's age, but raises an exception if age
    user_age = int(input())          # is less than 18 or greater than 75
    if user_age < 18 or user_age > 75:
        raise ValueError("Invalid age.")
    return user_age


try:                                 # try block of code that calls functions and prints output
    user_age = get_age()
    heart_rate = fat_burning_heart_rate(user_age)
    print("Fat burning heart rate for a {} year-old: {} bpm".format(user_age, heart_rate))

except ValueError as excpt:    # is executed when an exception is raised in a function
    print(excpt)
    print("Could not calculate heart rate info.\n")
