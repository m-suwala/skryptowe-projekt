import requests


def get_meals(name):
    try:
        meals = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s={}".format(name))
        meals_info = get_meals_info_list(meals)
        return meals_info
    except requests.exceptions.MissingSchema:
        return None


def get_meal(id):
    try:
        meal = requests.get("https://www.themealdb.com/api/json/v1/1/lookup.php?i={}".format(id))
        meal_info = get_meals_info_list(meal)
        return meal_info
    except requests.exceptions.MissingSchema:
        return None

def get_random_meal():
    try:
        meal = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
        meal_info = get_meals_info_list(meal)
        return meal_info
    except Exception:
        return None


def get_meals_by_category(category):
    try:
        meals = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c={}".format(category))
        return meals.json()['meals']
    except requests.exceptions.MissingSchema:
        return None


def get_meals_by_ingredient(ingredient):
    try:
        meals = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?i={}".format(ingredient))
        return meals.json()['meals']
    except requests.exceptions.MissingSchema:
        return None


def get_meals_by_cuisine(cuisine):
    try:
        meals = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?a={}".format(cuisine))
        return meals.json()['meals']
    except requests.exceptions.MissingSchema:
        return None


def get_list_of_categories():
    try:
        categories = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?c=list").json()
        return categories['meals']
    except Exception:
        return None


def get_list_of_cuisines():
    try:
        cuisines = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?a=list").json()
        return cuisines['meals']
    except Exception:
        return None


def get_list_of_ingredients():
    try:
        ingredients = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?i=list").json()
        return ingredients['meals']
    except Exception:
        return None


# called by the get_meals
# gives only needed info
def get_meals_info_list(meal):
    meals = meal.json()['meals']
    meals_list = []
    if meals:
        for m in meals:
            name = m['strMeal']
            category = m['strCategory']
            cuisine = m['strArea']
            instructions = format_text(m['strInstructions'])
            image = m['strMealThumb']
            ingredients = ""
            for i in range(1, 21):
                ingr = m['strIngredient{}'.format(i)]
                amount = m['strMeasure{}'.format(i)]
                if ingr != "" and amount != "":
                    ingredients += amount + " " + ingr + "\n"
                else:
                    break
            meals_list.append({"name": name, "category": category, "cuisine": cuisine, "ingredients": ingredients, "instructions": instructions, "image": image})
    return meals_list


def format_text(text):
    result = ""
    words = text.split(" ")
    for i in range(30, len(text), 35):
        words.insert(i, "\n")
    for i in range(0, len(words)):
        result += words[i] + " "
    return result


def print_meals(meals):
    for m in meals:
        print("name: " + m['name'])
        print("category: " + m['category'])
        print("cuisine: " + m['cuisine'])
        print("ingredients: ")
        for ingr, amount in m["ingredients"]:
            print(amount, ingr)
        print("instructions: " + m['instructions'])
