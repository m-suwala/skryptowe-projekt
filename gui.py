from tkinter import *
import io
from PIL import Image, ImageTk
import requests
import api_functions

BUTTON_C = '#D6E9E9'
BG_C = '#A1CCD7'


def next_recipe(window, id, meals=None, names=None):
    window.destroy()
    if meals:
        open_recipe_window(id+1, meals=meals)
    if names:
        open_recipe_window(id+1, names=names)


def previous_recipe(window, id, meals=None, names=None):
    window.destroy()
    if meals:
        open_recipe_window(id-1, meals=meals)
    if names:
        open_recipe_window(id-1, names=names)


def open_recipe_window(id, meals=None, names=None):
    recipe_window = Toplevel()

    if meals:
        meal = meals[id]
    else:
        meal = api_functions.get_meal(names[id]['idMeal'])[0]

    canvas = Canvas(recipe_window, height=650, width=1200, bg=BG_C)
    canvas.pack(fill='both', expand=True)

    recipe_window.title(meal['name'])

    label_name = Label(recipe_window, text=meal['name'], bg=BG_C, font='{Bradley Hand ITC} 30')
    label_name.place(relx=0, rely=0, relwidth=0.4, relheight=0.1)

    label_category = Label(recipe_window, text="category: " + meal['category'], bg=BG_C, font='Cambria')
    label_category.place(relx=0, rely=0.1, relwidth=0.2, relheight=0.1)

    label_cuisine = Label(recipe_window, text="cuisine: " + meal['cuisine'], bg=BG_C, font='Cambria')
    label_cuisine.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.1)

    label_ingredients = Label(recipe_window, text="ingredients:\n " + meal['ingredients'], bg=BG_C, font='Cambria 8')
    label_ingredients.place(relx=0, rely=0.2, relwidth=0.4)

    label_instructions = Label(recipe_window, text="instructions:\n" + meal['instructions'], bg=BG_C, font='Cambria 8')
    label_instructions.place(relx=0, rely=0.5, relwidth=1)

    response = requests.get(meal['image'])
    image_bytes = io.BytesIO(response.content)
    myimage = Image.open(image_bytes)
    myimage = myimage.resize((400, 400))
    im = ImageTk.PhotoImage(myimage)

    label_image = Label(recipe_window, image=im, bg=BG_C)
    label_image.place(relx=0.5, rely=0.03, relwidth=0.6, relheight=0.45)

    # next button
    right = Image.open("right.png")
    right = right.resize((80, 30))
    img_right = ImageTk.PhotoImage(right)
    if meals:
        button_next = Button(recipe_window, text="Button", image=img_right, command=lambda: next_recipe(recipe_window, id, meals=meals), bg=BUTTON_C)
    else:
        button_next = Button(recipe_window, text="Button", image=img_right, command=lambda: next_recipe(recipe_window, id, names=names), bg=BUTTON_C)
    if (meals and len(meals)-1 > id) or (names and len(names)-1 > id):
        button_next.place(relx=0.97, rely=0.95, relwidth=0.05, relheight=0.05, anchor='e')

    # previous button
    left = Image.open("left.png")
    left = left.resize((80, 30))
    img_left = ImageTk.PhotoImage(left)
    if meals:
        button_prev = Button(recipe_window, text="Button", image=img_left, command=lambda: previous_recipe(recipe_window, id, meals=meals), bg=BUTTON_C)
    else:
        button_prev = Button(recipe_window, text="Button", image=img_left, command=lambda: previous_recipe(recipe_window, id, names=names), bg=BUTTON_C)
    if id != 0:
        button_prev.place(relx=0.03, rely=0.95, relwidth=0.05, relheight=0.05, anchor='w')

    recipe_window.mainloop()


def open_categories_window():

    def category_clicked(category):
        meals = api_functions.get_meals_by_category(category)
        open_recipe_window(0, names=meals)

    categories_window = Toplevel()
    categories_window.title("Categories")

    canvas = Canvas(categories_window, height=400, width=600, bg=BG_C)
    canvas.pack()

    label_categories = Label(categories_window, text="Categories", bg=BG_C, font='{Bradley Hand ITC} 30')
    label_categories.place(relx=0, rely=0.05, relwidth=1)

    categories = api_functions.get_list_of_categories()

    categories_buttons = []
    for i in range(0, len(categories)):
        button = Button(categories_window, text=categories[i]['strCategory'],
                        command=lambda message=categories[i]['strCategory']: category_clicked(message), bg=BUTTON_C, font='Cambria')
        categories_buttons.append(button)

    i = 0
    j = 0
    id = 0
    count = 0
    for button in categories_buttons:
        button.place(relx=0.05 + i, rely=0.3 + j, relwidth=0.2, relheight=0.1)
        id += 1
        i += 0.23
        count += 1
        if count == 4:
            j += 0.15
            count = 0
            i = 0

    categories_window.mainloop()


def open_cuisines_window():

    def cuisine_clicked(cuisine):
        meals = api_functions.get_meals_by_cuisine(cuisine)
        open_recipe_window(0, names=meals)

    cuisines_window = Toplevel()

    cuisines_window.title("Cuisines")

    canvas = Canvas(cuisines_window, height=400, width=600, bg=BG_C)
    canvas.pack()

    label_cuisines = Label(cuisines_window, text="Cuisines", bg=BG_C, font='{Bradley Hand ITC} 30')
    label_cuisines.place(relx=0, rely=0.05, relwidth=1)

    cuisines = api_functions.get_list_of_cuisines()

    cuisines_buttons = []
    for i in range(0, len(cuisines)):
        button = Button(cuisines_window, text=cuisines[i]['strArea'],
                        command=lambda message=cuisines[i]['strArea']: cuisine_clicked(message), bg=BUTTON_C, font='Cambria')
        cuisines_buttons.append(button)

    i = 0
    j = 0
    id = 0
    count = 0
    for button in cuisines_buttons:
        button.place(relx=0.05 + i, rely=0.2 + j, relwidth=0.2, relheight=0.1)
        id += 1
        i += 0.23
        count += 1
        if count == 4:
            j += 0.11
            count = 0
            i = 0

    cuisines_window.mainloop()


root = Tk()
root.title('RECIPES')

canvas = Canvas(root, height=400, width=600, bg=BG_C)
canvas.pack()

frame_title = Frame(root, bg=BG_C)
frame_title.place(relx=0, rely=0, relwidth=1, relheight=0.2)

label_title = Label(frame_title, text="RECIPES", font='{Bradley Hand ITC} 30', bg=BG_C)
label_title.pack(fill='both', expand=True)

frame_choosing = Frame(root, bg=BG_C)
frame_choosing.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.8)

button_random = Button(frame_choosing, text="Go to random recipe", command=lambda: open_recipe_window(0, meals=api_functions.get_random_meal()), bg=BUTTON_C, font='Cambria')
button_random.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

label_see = Label(frame_choosing, text="See list of all:", bg=BG_C, font='Cambria')
label_see.place(relx=0.1, rely=0.31, relwidth=0.8, relheight=0.1)

button_categories = Button(frame_choosing, text="Categories", command= lambda: open_categories_window(), bg=BUTTON_C, font='Cambria')
button_categories.place(relx=0.1, rely=0.46, relwidth=0.8, relheight=0.1)

button_cuisines = Button(frame_choosing, text="Cuisines", command= lambda: open_cuisines_window(), bg=BUTTON_C, font='Cambria')
button_cuisines.place(relx=0.1, rely=0.57, relwidth=0.8, relheight=0.1)

button_ingredients = Button(frame_choosing, text="Ingredients", bg=BUTTON_C, font='Cambria')
button_ingredients.place(relx=0.1, rely=0.68, relwidth=0.8, relheight=0.1)


frame_log = Frame(root, bg=BG_C)
frame_log.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.8)


def search(name):
    label_fail = Label(frame_log, bg=BG_C)
    label_fail.place(relx=0.1, rely=0.7, relwidth=0.7, relheight=0.1)
    meals = api_functions.get_meals(name)
    if meals:
        open_recipe_window(0, meals=meals)
        label_fail.configure(text="")
    else:
        label_fail.configure(text="There are no recipes for " + name)


button_login = Button(frame_log, text="LOG IN", bg=BUTTON_C, font='Cambria')
button_login.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.1)

button_signup = Button(frame_log, text="SIGN UP", bg=BUTTON_C, font='Cambria')
button_signup.place(relx=0.1, rely=0.26, relwidth=0.8, relheight=0.1)

label_search = Label(frame_log, text="Search:", bg=BG_C, font='Cambria')
label_search.place(relx=0.1, rely=0.51, relwidth=0.8, relheight=0.1)

entry_search = Entry(frame_log, font='Cambria')
entry_search.place(relx=0.1, rely=0.62, relwidth=0.7, relheight=0.1)

button_search = Button(frame_log, text="GO", command=lambda: search(entry_search.get()), bg=BUTTON_C, font='Cambria')
button_search.place(relx=0.85, rely=0.62, relwidth=0.1, relheight=0.1)

root.mainloop()
