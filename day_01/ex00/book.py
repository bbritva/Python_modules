import sys
import datetime

from recipe import Recipe


class Book:
    def validate_params(self):
        """Return the error description in case of error"""
        if not self.name:
            return ("empty name")
        if not isinstance(self.name, str):
            return ("name is not a string")
        return ''

    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}
        err = self.validate_params()
        if err:
            raise ValueError(err)

    def __str__(self):
        """Return the string to print cookbook info"""
        txt = '\n'.join([f'CookBook named {self.name}:',
                         f'   Last update time {self.last_update.strftime("%H:%M:%S")};',
                         f'   Creation time    {self.creation_date.strftime("%H:%M:%S")}.'])
        return txt

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for type in self.recipes_list.keys():
            for dish in self.recipes_list[type]:
                if dish.name == name:
                    print(dish)
                    return dish
        print("Dish is not found =(")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list.keys():
            return self.recipes_list[recipe_type]
        else:
            print('Wrong type of recipe (should be "starter", "lunch" or "dessert")')

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)
            print(f'Recipe {recipe.name} added.')
            self.last_update = datetime.datetime.now()
        else:
            print("Argument is not a Recipe")
