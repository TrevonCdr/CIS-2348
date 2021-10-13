# Trevon McKenzie
# 1880601

coefficients = []
num_coefficients = 6
solved = 'no'

while len(coefficients) < 6:                             # converts each input element from
    element = int(input())                               # string to integer and appends it to the
    coefficients.append(element)                         # list

for x in range(-10, 11):        # outer for loop iterates through x values
   for y in range(-10, 11):     # inner for loop iterates through y values
      if (coefficients[0] * x) + (coefficients[1] * y) == coefficients[2]:      # inserts x and y values into equations
         if (coefficients[3] * x) + (coefficients[4] * y) == coefficients[5]:   # to check validity
            print(x, y)     #prints x and y values that satisfy equations
            solved = 'yes'
         else:
            pass
      else:
         pass
else:                      # Checks if equation was solved
   if solved != 'yes':
      print("No solution")