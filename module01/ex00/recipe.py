class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = f"Recipe : {self.name}\n"
        txt += f"Cooking level : {self.cooking_lvl}\n"
        txt += f"Cooking time : {self.cooking_time} min\n"
        txt += f"Ingredients : {self.ingredients}\n"
        txt += f"Description : {self.description}\n"
        txt += f"Recipe type : {self.recipe_type}"
        return txt