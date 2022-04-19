from flask import Flask, render_template, request
import csv_reader_writer as csv

app = Flask(__name__)
#TODO add picture functionality
#TODO add csv read and write function
#TODO create add recipe page
    #TODO add js validation for adding recipes
#TODO create edit recipe page
#TODO create remove recipe page
#TODO add links based on list position (cookie is recipez[0]/cake is recipez[1](done)

recipe_list_csv = [["cookie", "dessert", "cookie.png", ["butter", "flour"], ["blend together", "bake at 375"]],
           ["cake", "dessert","cake.png", ["butter", "flour", "egg"], ["blend", "bake at 450"]],
           ["muffin", "dessert", "muffin.png", ["butter", "bran"], ["mix", "bake at 325"]]]
'''
csv.write_to_csv(recipe_list_csv)
recipe_list = []
recipe_list = csv.read_csv()
'''

recipe_list = recipe_list_csv
header = "yo its the recipe page"


@app.route("/")
def home():
    recipe_links = []
    for recipe in recipe_list:
        recipe_links.append(recipe[0])

    return render_template("Home.html", header=header, recipe_links=recipe_links)


@app.route("/<string:recipe_name>")
def recipes(recipe_name):
    index = 0
    for recipe in recipe_list:
        if recipe[0] == recipe_name:
            index = recipe_list.index(recipe)
    recipe_name = recipe_list[index][0]
    recipe_type = recipe_list[index][1]
    image = recipe_list[index][2]
    ingredients = recipe_list[index][3]
    prep_instructions = recipe_list[index][4]
    return render_template("recipe_page_layout.html", recipe_name=recipe_name, recipe_type=recipe_type, image=image,
                           ingredients=ingredients, prep_instructions=prep_instructions)


@app.route("/add")
def add_recipe():
    return render_template("add_recipe.html")


@app.route("/submit", methods=["POST"])
def submit():
    recipe = []
    name = request.form.get('recipe_name')
    recipe.append(name)
    img = name + ".png" #TODO add picture input functionality
    recipe.append(img)
    type = request.form.get('recipe_type')
    recipe.append(type)
    ingredients = request.form.get('ingredients')
    ingredient_list = string_to_list(ingredients)
    recipe.append(ingredient_list)
    prep = request.form.get('prep')
    prep_list = string_to_list(prep)
    recipe.append(prep_list)
    recipe_list.append(recipe)
    return render_template("submit.html", name=name, type=type, ingredients=ingredient_list)

'''
@app.route("/edit/<string:recipe_name>")
def edit(recipe_name):
    index = 99
    for recipe in recipe_list:
        if recipe[0] == recipe_name:
            index = recipe_list.index(recipe)
    recipe_name = recipe_list[index][0]
    recipe_type = recipe_list[index][1]
    image = recipe_list[index][2]
    ingredients = recipe_list[index][3]
    prep_instructions = recipe_list[index][4]
    return render_template("edit_recipe.html", recipe_name=recipe_name, recipe_type=recipe_type, image=image,
                           ingredients=ingredients, prep_instructions=prep_instructions)
'''

@app.route("/remove/<string:recipe_name>")
def remove(recipe_name):
    for recipe in recipe_list:
        if recipe[0] == recipe_name:
            index = recipe_list.index(recipe)
            recipe_list.pop(index)
    return render_template("remove_recipe.html", recipe_name=recipe_name)


def string_to_list(string):
    create_list = list(string.split(", "))
    return create_list




if __name__ == '__main__':
    app.run()
