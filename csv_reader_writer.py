import csv


def write_to_csv(recipe_list):
    recipe_guide = ["recipe_name", "recipe_type", "recipe_image", "ingredient_list", "prep_instructions_list"]
    with open("recipe_list.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(recipe_list)


def read_csv():
    recipe_list =[]
    with open("recipe_list.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            recipe_list.append(row)
    print_csv(recipe_list)

    return recipe_list


def print_csv(recipe_list):
    for recipe in recipe_list:
        print(recipe)


def list_to_string(recipe_list):
    recipe_string = ""
    for recipe in recipe_list:
        recipe_string += recipe

