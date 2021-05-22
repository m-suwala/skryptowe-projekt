import requests


def get_meals(name):
    try:
        return requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s={}".format(name))
    except requests.exceptions.MissingSchema:
        return None


def get_meals_starting_with(letter):
    try:
        return requests.get("https://www.themealdb.com/api/json/v1/1/search.php?f={}".format(letter))
    except requests.exceptions.MissingSchema:
        return None


def get_random_meal():
    try:
        return requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    except Exception:
        return None


def get_list_of_categories():
    try:
        return requests.get("https://www.themealdb.com/api/json/v1/1/list.php?c=list")
    except Exception:
        return None


def get_list_of_cuisines():
    try:
        return requests.get("https://www.themealdb.com/api/json/v1/1/list.php?a=list")
    except Exception:
        return None


def get_list_of_ingredients():
    try:
        return requests.get("https://www.themealdb.com/api/json/v1/1/list.php?i=list")
    except Exception:
        return None


def get_meals_by_ingredient(ingredient):
    try:
        return requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?i={}".format(ingredient))
    except requests.exceptions.MissingSchema:
        return None


def get_meals_by_category(category):
    try:
        return requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c={}".format(category))
    except requests.exceptions.MissingSchema:
        return None


def get_meals_by_cuisine(cuisine):
    try:
        return requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?a={}".format(cuisine))
    except requests.exceptions.MissingSchema:
        return None


def get_meal_info(meal):
    meals = meal.json()['meals']
    meals_list = []
    for m in meals:
        name = m['strMeal']
        category = m['strCategory']
        cuisine = m['strArea']
        instructions = m['strInstructions']
        image = m['strMealThumb']
        meals_list.append({"name": name, "category": category, "cuisine": cuisine, "instructions": instructions, "image": image})
    return meals_list


def get_meal_name(meal_info):
    return meal_info["name"]


def get_meal_category(meal_info):
    return meal_info["category"]


def get_meal_cuisine(meal_info):
    return meal_info["cuisine"]


def get_meal_instructions(meal_info):
    return meal_info["instructions"]


def get_meal_image(meal_info):
    return meal_info["image"]


def print_meals(meals):
    for m in meals:
        print("name: " + m['name'])
        print("category: " + m['category'])
        print("cuisine: " + m['cuisine'])
        print("instructions: " + m['instructions'])


# get list of all meals sorted in categories -
# same but with cuisines
# same but alphabet - so that i can make a "book" and you can choose recipes on a letter a, b, c...
# okay nah idk if i want all that


if __name__ == '__main__':
    string = "hrafas asg t afdgsf ef, DSG we, ga"
    s = string[9:20].find(" ")
    print(s)


