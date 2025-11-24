import sys

cookbook = {
    'Sandwich': {
        'ingredients': ('ham', 'bread', 'cheese', 'tomatoes'),
        'meal': 'lunch',
        'prep_time': 10
    },
    'Cake': {
        'ingredients': ('lour', 'sugar', 'eggs'),
        'meal': 'dessert',
        'prep_time': 60
    },
    'Salad': {
        'ingredients': ('avocado', 'arugula', 'tomatoes', 'spinach'),
        'meal': 'lunch',
        'prep_time': 15
    }
}

for recipe in cookbook:
    print(f"{recipe}")

for recipe in cookbook:
    if sys.argv[1] == recipe:
        print(f"{recipe[0]}")
        print(f"{recipe[1]}")
        print(f"{recipe[2]}")