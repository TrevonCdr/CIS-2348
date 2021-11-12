# Trevon McKenzie
# 1880601

class FoodItem:        # create class FoodItem with instance methods get_calories and print_info
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name                        # assign attributes with values
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings=1.00):  # calculate calories based on the number of servings
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):      # print out nutritional information
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings, go_time.get_calories(servings)))


food_name = input()              # get new values from input
grams_fat = float(input())
grams_carbs = float(input())
grams_protein = float(input())
servings = float(input())

go_time = FoodItem()
go_time.print_info()
print()

go_time = FoodItem(food_name, grams_fat, grams_carbs, grams_protein)
go_time.print_info()  # print new nutritional information


