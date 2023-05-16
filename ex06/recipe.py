import sys

cookbook = {
    'Sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'Cake': {
        'ingredients': ['flour', 'sugar', 'egg'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'Salad': {
        'ingredients': ['avoca', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}

def print_recipe_names(cookbook=None):
    for recipe in cookbook:
        print("\n")
        print(recipe)

def print_recipe_details(cookbook, recipe_name):
    if recipe_name in cookbook:
        print(f"\nRecipe Name: {recipe_name}")
        print(f"Ingredients: {cookbook[recipe_name]['ingredients']}")
        print(f"Meal type: {cookbook[recipe_name]['meal']}")
        print(f"Preparation time: {cookbook[recipe_name]['prep_time']}")
    else:
        print(f"{recipe_name} is not in the cookbook.")

def delete_recipe(cookbook, recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print(f"\n{recipe_name} has been deleted from the cookbook.")
    else:
        print(f"\n{recipe_name} is not in the cookbook.")

def add_recipe(cookbook):
    recipe_name = ""
    ingredients = []
    meal = ""
    prep_time = ""
    while recipe_name == "":
        recipe_name = input("\nPlease enter the name of the recipe: \n")
    ingredient = None
    print("\nEnter ingredients (enter new line when finished):")
    while True:
        ingredient = input()
        if (ingredient == ''): 
            break
        ingredients.append(ingredient)
    while meal == "":
        meal = input("\nPlease enter the meal type: \n")
    while True:
        prep_time = input("\nPlease enter the preparation time (in minutes): \n")
        if not prep_time:
            print("You must provide a preparation time.\n")
        else:
            try:
                prep_time = int(prep_time)
                break
            except ValueError:
                print("\n**-.Preparation time must be a number.-**")
    cookbook[recipe_name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }
    print(f"\n{recipe_name} has been added to the cookbook.")

if __name__ == "__main__":
        print("\nWelcome to the Python Cookbook!\n")
        print("  List of available options:")
        print("   1: Add a recipe")
        print("   2: Delete a recipe")
        print("   3: Print a recipe")
        print("   4: Print the cookbook")
        print("   5: Quit\n")
        while True:
            user_choice = input("\n\n>>Please select an option: \n\n")
            if user_choice == "1":
                add_recipe(cookbook)
            elif user_choice == "2":
                recipe_name = input("\n>>>Please enter the name of the recipe to delete:  \n\n")
                delete_recipe(cookbook, recipe_name)
            elif user_choice == "3":
                recipe_name = input("\n>>>Please enter the name of the recipe to print:  \n\n")
                print_recipe_details(cookbook, recipe_name)
            elif user_choice == "4":
                print_recipe_names(cookbook)
            elif user_choice == "5":
                print("\n Goodbye!\n\n")
                sys.exit()
            else:
                print("\n**-.Sorry, this option doesn't exist. Please try again.-**  \n")