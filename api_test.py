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

def get_meal(id):
    try:
        meal = requests.get("https://www.themealdb.com/api/json/v1/1/lookup.php?i={}".format(id))
        return meal
    except requests.exceptions.MissingSchema:
        return None

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
                    ingredients += ingr + " " + amount + "\n"
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


def get_meals_by_category(category):
    try:
        meals = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c={}".format(category))
        meal_list = []
        for meal in meals.json()['meals']:
            meal_list.append(get_meals_info_list(get_meal(meal['idMeal'])))
        return meal_list
    except requests.exceptions.MissingSchema:
        return None

def print_meal(m):
    print("name: " + m[0]['name'])
    print("category: " + m[0]['category'])
    print("cuisine: " + m[0]['cuisine'])
    print("instructions: " + m[0]['instructions'])

if __name__ == '__main__':
    meals = get_meals_by_category("Beef")
    for meal in meals:
        print_meal(meal)



