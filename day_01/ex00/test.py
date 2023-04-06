from time import sleep
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
    print("\n".join([scramble.__str__(), rice.__str__(), cake.__str__()]))

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

