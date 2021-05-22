import io
from tkinter import *
from PIL import Image, ImageTk
import requests

import api_functions
HEIGHT = 500
WIDTH = 700


recipe_window = Tk()

canvas = Canvas(recipe_window, height=600, width=1200)
canvas.pack()

meals = api_functions.get_meals('french')


recipe_window.title(meals[0]['name'])


label_name = Label(recipe_window, text=meals[0]['name'], font=34)
label_name.place(relx=0, rely=0.05, relwidth=0.4, relheight=0.1)

label_category = Label(recipe_window, text="category: " + meals[0]['category'])
label_category.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.1)

label_cuisine = Label(recipe_window, text="cuisine: " + meals[0]['cuisine'])
label_cuisine.place(relx=0.2, rely=0.15, relwidth=0.2, relheight=0.1)

label_ingredients = Label(recipe_window, text="ingredients:\n " + meals[0]['ingredients'])
label_ingredients.place(relx=0, rely=0.25, relwidth=0.4) # relheight=0.5

label_instructions = Label(recipe_window, text="instructions:\n" + meals[0]['instructions'])
label_instructions.place(relx=0, rely=0.6, relwidth=1)

response = requests.get(meals[0]['image'])
image_bytes = io.BytesIO(response.content)
myimage = Image.open(image_bytes)
myimage = myimage.resize((400, 400))
im = ImageTk.PhotoImage(myimage)

label_image = Label(recipe_window, image=im)
label_image.place(relx=0.5, rely=0.03, relwidth=0.5, relheight=0.5)

# next button
right = Image.open("right.png")
right = right.resize((80, 30))
img_right = ImageTk.PhotoImage(right)
button_next = Button(recipe_window, text="Button", image=img_right)
button_next.place(relx=0.97, rely=0.95, relwidth=0.05, relheight=0.05, anchor='e')

# previous button
left = Image.open("left.png")
left = left.resize((80, 30))
img_left = ImageTk.PhotoImage(left)
button_prev = Button(recipe_window, text="Button", image=img_left)
button_prev.place(relx=0.03, rely=0.95, relwidth=0.05, relheight=0.05, anchor='w')

recipe_window.mainloop()