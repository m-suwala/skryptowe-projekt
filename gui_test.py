import io
from tkinter import *
from tkinter import font

from PIL import Image, ImageTk
import requests
import api_functions


def ingredients_clicked(cuisine):
    print(cuisine)


ingredients_window = Tk()

print(font.families())
ingredients_window.title("Ingredients")

canvas = Canvas(ingredients_window, height=400, width=600)
canvas.pack()

ingredients = api_functions.get_list_of_ingredients()



# ingredients_buttons = []
# for i in range(0, len(ingredients)):
#     button = Button(ingredients_window, text=ingredients[i]['strIngredient'], command=lambda message=ingredients[i]['strIngredient']: ingredients_clicked(message))
#     ingredients_buttons.append(button)
#
# i = 0
# j = 0
# id = 0
# count = 0
# for button in ingredients_buttons:
#     button.place(relx=i, rely=j, relwidth=0.04, relheight=0.03)
#     id += 1
#     i += 0.04
#     count += 1
#     if count == 22:
#         j += 0.04
#         count = 0
#         i = 0


ingredients_window.mainloop()
