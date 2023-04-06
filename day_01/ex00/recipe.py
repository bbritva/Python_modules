import sys


class Recipe:
    def validate_params(self):
        """Return the error description in case of error"""
        if not self.name:
            return("ERROR: empty name")
        if not isinstance(self.name, str):
            return("ERROR: name is not a string")
        if not isinstance(self.cooking_lvl, int):
            return("ERROR: cooking_lvl is not a number")
        if self.cooking_lvl < 1 or self.cooking_lvl > 5:
            return("ERROR: cooking_lvl should be from 1 to 5")
        if not isinstance(self.cooking_time, int):
            return("ERROR: cooking_time is not a number")
        if self.cooking_time < 1:
            return("ERROR: cooking_time should be over 0")
        if not isinstance(self.ingredients, list):
            return("ERROR: ingredients is not a list")
        if len(self.ingredients) == 0:
            return("ERROR: ingredients couldn't be empty")
        if not isinstance(self.description, str):
            return("ERROR: description is not a string")
        if not self.recipe_type in ["starter", "lunch", "dessert"]:
            return("ERROR: wrong recipe_type")
        return ''

    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        err = self.validate_params()
        if err:
            print(err)
            sys.exit(0)

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = '\n'.join([f'Recipe for {self.name}:',
                         '  - Ingredients list: {};'.format(', '.join(self.ingredients)),
                         f'  - To be eaten for {self.recipe_type};',
                         f'  - Takes {self.cooking_time} minutes of cooking;',
                         f'  - Has difficulty level {self.cooking_lvl}.'])
        return txt


rec = Recipe("rr", 3, 3, ["hh", "gg"], "", "starter")
print(rec)
