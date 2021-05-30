from PyQt5 import QtGui
from recipeWindowGUI import Ui_Form
import urllib.request
import api_functions as api


class RecipeWindow():
    def __init__(self, window, meals, id, is_meal):
        self.ui = Ui_Form()
        self.ui.setupUi(window)
        self.update_buttons()
        self.meals = meals
        self.id = id
        self.is_meal = is_meal


    def update_buttons(self):
        self.ui.next_pushButton.clicked.connect(self.next_recipe)
        self.ui.previous_pushButton.clicked.connect(self.prev_recipe)

    def next_recipe(self):
        self.id += 1
        self.load_recipe()

    def prev_recipe(self):
        self.id -= 1
        self.load_recipe()

    def load_recipe(self):
        if self.is_meal:
            meal = self.meals[self.id]
        else:
            meal = api.get_meal(self.meals[self.id]['idMeal'])[0]

        self.ui.title_label.setText(meal['name'])
        self.ui.category_label.setText(meal['category'])
        self.ui.cuisine_label.setText(meal['cuisine'])
        self.ui.ingredients.clear()
        for ing in meal['ingredients']:
            self.ui.ingredients.addItem(ing)
        self.ui.instructions.setText(meal['instructions'])
        self.ui.next_pushButton.hide()
        self.ui.previous_pushButton.hide()

        url = meal['image']
        data = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        pixmap = QtGui.QPixmap(image)
        self.ui.photo_label.setPixmap(pixmap.scaledToHeight(400))

        if len(self.meals)-1 > self.id:
            self.ui.next_pushButton.show()
        if self.id != 0:
            self.ui.previous_pushButton.show()
