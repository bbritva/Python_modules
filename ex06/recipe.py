cookbook = {'sandwich': (['ham', 'bread', 'cheese', 'tomatoes'], 'lunch', '10'),
            'cake': (['flour', 'sugar', 'eggs'], 'dessert', '60'),
            'salad': (['avocado', 'arugula', 'tomatoes', 'spinach'], 'lunch', '15')}

def print_names():
    line  = ', '.join('{}'.format(key) for key in cookbook.keys())
    print(line)

def print_recipe(dish_name):
    dish = cookbook.get(dish_name)
    if (dish):
        print('Recipe for {}:'.format(dish_name))
        print('   Ingredients list: ', dish[0])
        print('   To be eaten for {}.'.format(dish[1]))
        print('   Takes {} minutes of cooking.'.format(dish[2]))
    else:
        print('Invalid recipe name.')

def delete_recipe(dish_name):
    if dish_name in cookbook.keys():
        del cookbook[dish_name]
        print('Recipe of {} deleted.'.format(dish_name))
    else:
        print('Invalid recipe name.')

def add_recipe():
    name = input('Enter a name:\n')
    ingredients = []
    ing = input('Enter ingredients:\n')
    while ing:
        ingredients.append(ing)
        ing = input()
    meal_type = input('Enter meal type:\n')
    prep_time = 0
    while True:
        try:
            prep_time = int(input('Enter preparation time:\n'))
            break
        except ValueError:
            continue
    cookbook[name] = [ingredients, meal_type, prep_time]


if __name__ == "__main__":
    print("""Welcome to the Python Cookbook !\nList of available option:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit""")
    option = 0;
    while True:
        try:
            option = int(input('Please select an option:\n>> '))
        except ValueError:
            option = 0

        if option == 1:
            add_recipe()
        elif option == 2:
            dish_name = input('Enter name of recipe to delete:\n>> ')
            delete_recipe(dish_name)
        elif option == 3:
            dish_name = input('Enter name of recipe to print:\n>> ')
            print_recipe(dish_name)
        elif option == 4:
            for key in cookbook.keys():
                print_recipe(key)
        elif option == 5:
            print('Cookbook closed. Goodbye !')
            break
        else:
            print('Sorry, this option does not exist.')
