# Trevon McKenzie
# 1880601

import math

wall_height = float(input("Enter wall height (feet):\n")) #Stores input value of wall height and
wall_width = float(input("Enter wall width (feet):\n"))   #wall width in variables

wall_area = int(wall_height * wall_width)                  #Calculate wall area and output its value
print("Wall area:", wall_area, "square feet")

needed_paint = wall_area / 350                             #Calculates needed paint in gallons
print("Paint needed: {:.2f} gallons".format(needed_paint)) #and outputs value with two spaces after decimal

needed_cans = math.ceil(needed_paint)                      #Rounds up the needed paint value to
print("Cans needed:", needed_cans, "can(s)\n")             #calculate needed number of paint cans

paint_color = input("Choose a color to paint the wall:\n")
paint_cost = {'red': 35, 'blue': 25, 'green': 23}          #Associates paint color with cost per can
print("Cost of purchasing {} paint: ${}".format(paint_color, paint_cost[paint_color] * needed_cans))

