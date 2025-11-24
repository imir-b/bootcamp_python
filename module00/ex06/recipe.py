import sys

cookbook = {
    'Sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'Cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'Salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}

def print_cookbook():
    for recipe in cookbook:
        print(f"{recipe}")

def print_recipe(recipe):
    print(f"Recipe: {recipe}")
    details = cookbook[recipe]
    print(f"Ingredients list: {details['ingredients']}")
    print(f"To be eaten for {details['meal']}.")
    print(f"Takes {details['prep_time']} minutes of cooking.")

def del_recipe(recipe):
    del(cookbook[recipe])

def add_recipe():
    name = input(">>> Enter a name:")
    ingredients = input(">>> Enter ingredients:").split(',')
    meal = input(">>> Enter a meal type:")
    ptime = int(input(">>> Enter a preparation time:"))
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': ptime
    }

if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")

    while True:
        print("List of available options:")
        print("\t1: Add a recipe")
        print("\t2: Delete a recipe")
        print("\t3: Print a recipe")
        print("\t4: Print the cookbook")
        print("\t5: Quit")

        try:
            option = int(input(">>> Please select an option:"))
        except ValueError:
            print("ValueError, this option is not valid.")
            continue

        if option == 1:
            add_recipe()

        elif option == 2:
            name = input(">>> Please enter a recipe to delete it:")
            if name in cookbook:
                del_recipe(name)
            else:
                print("Sorry, this recipe does not exist.")

        elif option == 3:
            name = input(">>> Please enter a recipe name to get its details:")
            if name in cookbook:
                print_recipe(name)
            else:
                print("Sorry, this recipe does not exist.")

        elif option == 4:
            print_cookbook()

        elif option == 5:
            print("Cookbook closed. Goodbye!")
            sys.exit(0)

        else:
            print("Sorry, this option is not valid.")
