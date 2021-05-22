from tkinter import *
import api_functions
HEIGHT = 400
WIDTH = 600


def search(name):
    meals = api_functions.get_meals(name)

    recipe_window = Toplevel()
    recipe_window.title(meals[0]['name'])

    label_name = Label(recipe_window, text=meals[0]['name'], font='Mistral 30')
    label_name.place(relx=0, rely=0, relwidth=0.8, relheight=0.1)


    api_functions.print_meals(meals)


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
