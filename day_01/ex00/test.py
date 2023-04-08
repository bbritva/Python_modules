from time import sleep

from termcolor import cprint
from book import Book
from recipe import Recipe


if __name__ == '__main__':
    print("Recipe tests:\n")
    # print("Bad parameters:")
    # badRecipe = Recipe("Scramble", 3, 20, 0, "", "lunch")
    # badRecipe = Recipe("Scramble", 3, 20, ['eggs', 'oil', 'salt'], "", "lunchee")
    # badRecipe = Recipe("Scramble", 3, -20, ['eggs', 'oil', 'salt'], "", "lunch")
    # badRecipe = Recipe("", 3, 20, ['eggs', 'oil', 'salt'], "", "lunch")

    print("Good parameters:")
    scramble = Recipe("Scramble", 2, 20, ['eggs', 'oil', 'salt'], "", "lunch")
    rice = Recipe("Rice", 1, 10, ['rice', 'water'], "", "starter")
    cake = Recipe("Cake", 3, 20, ['flour', 'water', 'sugar'], "", "dessert")
    print("\n".join([Book.recipe_to_str(scramble), Book.recipe_to_str(rice), Book.recipe_to_str(cake)]))

    print("\n\nBook tests:\n")
    print("Bad parameters:")
    try:
        book = Book(1)
    except ValueError as e:
        print("Error: ", e.args[0])
    try:
        book = Book("")
    except ValueError as e:
        print("Error: ", e.args[0])

    print("Good parameters:")

    book = Book("Book")
    print(book)
    print("waiting for 2 sec...\n")
    sleep(2)
    print("Add recipes to Book")
    book.add_recipe(scramble)
    book.add_recipe(rice)
    book.add_recipe(cake)
    print("Updated book:\n", book)

    print("\nAdd invalid Recipe to Book :")
    Book.add_recipe(book, 6)

    print("\nFind recipes in Book by type lunch")
    lunches = Book.get_recipes_by_types(book, 'lunch')
    for dish in lunches:
        print(dish)

    cprint("test from code_blocks", "white", "on_green")
    # cprint("### # 01.00.01", "green")
    # Recipe("cooki", 0, 10, ["dough", "sugar", "love"], "deliciousness incarnate", "dessert")
    # cprint("### # 01.00.02", "green")
    # Recipe("cooki", 1.5, 10, ["dough", "sugar", "love"], "deliciousness incarnate", "dessert")
    # cprint("### # 01.00.03", "green")
    # Recipe("cooki", 1, 10, [], "deliciousness incarnate", "dessert")
    cprint("### # 01.00.04", "green")
    Recipe("cooki", 1, 10, ["dough", "sugar", "love"], "deliciousness incarnate", "dessert")
    print("Congratulations you finally made sime delicous cookies")
    cprint("### # 01.00.05", "green")
    b = Book("My seductive recipes")
    print(b.creation_date)
    cprint("# should be the current date and time", "green")
    print(b.last_update)
    cprint("should be the same as the creation date or None", "green")
    cprint("### # 01.00.06", "green")
    crumble = Recipe("Crumble" , 1, 25, ["apples", "flour", "sugar"], "delicious", "dessert")
    b.add_recipe(crumble)
    print(b.last_update)
    cprint("### # 01.00.07", "green")
    print(b.get_recipe_by_name("Crumble"))
    cprint("# should print the recipe\n# AND\n# <Recipe object at x>", "green")
    b.get_recipe_by_name("Liver Icecream")
    cprint("# The recipe does not exist\n# The error must be handled in a justifiable manner", "green")
    cprint("### # 01.00.08", "green")
    print(Book.recipe_to_str(b.get_recipes_by_types("dessert")[0]))
    cprint("# Should print the Crumble recipe", "green")
    b.get_recipes_by_types("asdasd")
    cprint("# The recipe type does not exist, error must be handled in a justifiable manner", "green")


