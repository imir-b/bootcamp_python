import datetime

class Book:
    def __init__(self, name, recipe_list):
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.date.today()
        self.recipe_list = recipe_list

    def get_recipe_by_name(self, name):
        """Prints a recipe with the given name and returns the instance"""
        for recipe in self.recipe_list:
            if recipe.name == name:
                print(str(recipe)) 
                return recipe
        
        print(f"La recette '{name}' n'existe pas dans ce livre.")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type """
        result = []
        for recipe in self.recipe_list:
            if recipe.recipe_type == recipe_type:
                result.append(recipe.name)

        print(f"Recettes de type {recipe_type} : {result}")
        return result

    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""
        self.recipe_list.append(recipe)
        self.last_update = datetime.datetime.now()