from tkinter import *
import io
from PIL import Image, ImageTk
import requests
import api_functions

HEIGHT = 400
WIDTH = 600


def next_recipe(window, meals, id):
    window.destroy()
    open_recipe_window(meals, id+1)


def previous_recipe(window, meals, id):
    window.destroy()
    open_recipe_window(meals, id-1)


def open_recipe_window(meals, id):
    recipe_window = Toplevel()

    canvas = Canvas(recipe_window, height=600, width=1200)
    canvas.pack()

    recipe_window.title(meals[id]['name'])

    label_name = Label(recipe_window, text=meals[id]['name'], font=34)
    label_name.place(relx=0, rely=0, relwidth=0.4, relheight=0.1)

    label_category = Label(recipe_window, text="category: " + meals[id]['category'])
    label_category.place(relx=0, rely=0.1, relwidth=0.2, relheight=0.1)

    label_cuisine = Label(recipe_window, text="cuisine: " + meals[id]['cuisine'])
    label_cuisine.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.1)

    label_ingredients = Label(recipe_window, text="ingredients:\n " + meals[id]['ingredients'])
    label_ingredients.place(relx=0, rely=0.2, relwidth=0.4)

    label_instructions = Label(recipe_window, text="instructions:\n" + meals[id]['instructions'])
    label_instructions.place(relx=0, rely=0.5, relwidth=1)

    response = requests.get(meals[id]['image'])
    image_bytes = io.BytesIO(response.content)
    myimage = Image.open(image_bytes)
    myimage = myimage.resize((400, 400))
    im = ImageTk.PhotoImage(myimage)

    label_image = Label(recipe_window, image=im)
    label_image.place(relx=0.5, rely=0.03, relwidth=0.6, relheight=0.45)

    # next button
    right = Image.open("right.png")
    right = right.resize((80, 30))
    img_right = ImageTk.PhotoImage(right)
    button_next = Button(recipe_window, text="Button", image=img_right, command=lambda: next_recipe(recipe_window, meals, id))
    if len(meals)-1 > id:
        button_next.place(relx=0.97, rely=0.95, relwidth=0.05, relheight=0.05, anchor='e')

    # previous button
    left = Image.open("left.png")
    left = left.resize((80, 30))
    img_left = ImageTk.PhotoImage(left)
    button_prev = Button(recipe_window, text="Button", image=img_left, command=lambda: previous_recipe(recipe_window, meals, id))
    if id != 0:
        button_prev.place(relx=0.03, rely=0.95, relwidth=0.05, relheight=0.05, anchor='w')

    recipe_window.mainloop()


root = Tk()
root.title('RECIPES')

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame_title = Frame(root)
frame_title.place(relx=0, rely=0, relwidth=1, relheight=0.2)

label_title = Label(frame_title, text="RECIPES", font='Mistral 30')
label_title.pack(fill='both', expand=True)


frame_choosing = Frame(root)
frame_choosing.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.8)

button_all = Button(frame_choosing, text="See all recipes")
button_all.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

label_see = Label(frame_choosing, text="See list of all:")
label_see.place(relx=0.1, rely=0.31, relwidth=0.8, relheight=0.1)

button_categories = Button(frame_choosing, text="Categories")
button_categories.place(relx=0.1, rely=0.46, relwidth=0.8, relheight=0.1)

button_cuisines = Button(frame_choosing, text="Cuisines")
button_cuisines.place(relx=0.1, rely=0.57, relwidth=0.8, relheight=0.1)

button_ingredients = Button(frame_choosing, text="Ingredients")
button_ingredients.place(relx=0.1, rely=0.68, relwidth=0.8, relheight=0.1)


frame_log = Frame(root)
frame_log.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.8)


def search(name):
    label_fail = Label(frame_log)
    label_fail.place(relx=0.1, rely=0.7, relwidth=0.7, relheight=0.1)
    meals = api_functions.get_meals(name)
    if meals:
        open_recipe_window(meals, 0)
        label_fail.configure(text="")
    else:
        label_fail.configure(text="There are no recipes for " + name)


button_login = Button(frame_log, text="LOG IN")
button_login.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.1)

button_signup = Button(frame_log, text="SIGN UP")
button_signup.place(relx=0.1, rely=0.26, relwidth=0.8, relheight=0.1)

label_search = Label(frame_log, text="Search:")
label_search.place(relx=0.1, rely=0.51, relwidth=0.8, relheight=0.1)

entry_search = Entry(frame_log)
entry_search.place(relx=0.1, rely=0.62, relwidth=0.7, relheight=0.1)

button_search = Button(frame_log, text="GO", command=lambda: search(entry_search.get()))
button_search.place(relx=0.85, rely=0.62, relwidth=0.1, relheight=0.1)

root.mainloop()
