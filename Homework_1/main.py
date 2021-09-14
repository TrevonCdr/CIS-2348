# Trevon McKenzie
# 1880601

lemon_juice_cups = float(input("Enter amount of lemon juice (in cups):\n"))    #Receives cups of ingredients from
water_cups = float(input("Enter amount of water (in cups):\n"))                #user
agave_cups = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n\n"))

print("Lemonade ingredients - yields", '{:.2f}'.format(servings), "servings")  #Formats entered cups of ingredients
print('{:.2f}'.format(lemon_juice_cups), "cup(s) lemon juice")                 #with two spaces
print('{:.2f}'.format(water_cups), "cup(s) water")
print('{:.2f}'.format(agave_cups), "cup(s) agave nectar\n")

desired_servings = float(input("How many servings would you like to make?\n\n"))
desired_lemon_cups = ((desired_servings / servings) * lemon_juice_cups)            #Calculate needed cups of
desired_water_cups = ((desired_servings / servings) * water_cups)                  #ingredients for needed
desired_agave_cups = ((desired_servings / servings) * agave_cups)                  #servings

print("Lemonade ingredients - yields", '{:.2f}'.format(desired_servings), "servings")
print('{:.2f}'.format(desired_lemon_cups), "cup(s) lemon juice")                       #Output needed cups of
print('{:.2f}'.format(desired_water_cups), "cup(s) water")                             #ingredients
print('{:.2f}'.format(desired_agave_cups), "cup(s) agave nectar\n")

print("Lemonade ingredients - yields", '{:.2f}'.format(desired_servings), "servings")
print('{:.2f}'.format(desired_lemon_cups / 16), "gallon(s) lemon juice")               #Convert cups of ingredients
print('{:.2f}'.format(desired_water_cups / 16), "gallon(s) water")                     #into gallons
print('{:.2f}'.format(desired_agave_cups / 16), "gallon(s) agave nectar")
