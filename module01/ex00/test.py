from book import Book
from recipe import Recipe
import sys

# ... Your tests ...

def main():

    print("Give a name to your Recipe book")
    book_name = input(">>")
    myBook = Book(book_name, [])

    while True:
        print("Type 'ADD', 'GET NAME' or 'GET TYPE' to test")
        print("Type 'EXIT' to quit")
        command = input(">>")

        if command == "ADD":
            print("Enter the recipe name:")
            recipe_name = input(">>")
            print("Enter the cooking level (1-5):")
            cooking_lvl = int(input(">>"))
            print("Enter the cooking time (in minutes):")
            cooking_time = int(input(">>"))
            print("Enter the ingredients (comma-separated):")
            ingredients = input(">>").split(",")
            print("Enter the description:")
            description = input(">>")
            print("Enter the recipe type (starter, lunch, dessert):")
            recipe_type = input(">>")
            newRecipe = Recipe(recipe_name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
            try:
                myBook.add_recipe(newRecipe)
            except Exception as e:
                print(f"Error: {e}")

        elif command == "GET NAME":
            print("Get recipe by name:")
            name = input(">>")
            try:
                myBook.get_recipe_by_name(name)
            except Exception as e:
                print(f"Error: {e}")

        elif command == "GET TYPE":
            print("Get recipe by type:")
            type = input(">>")
            try:
                myBook.get_recipes_by_types(type)
            except Exception as e:
                print(f"Error: {e}")

        elif command == "EXIT":
            sys.exit(0)

if __name__ == "__main__": 
    main()