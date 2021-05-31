from PyQt5 import QtGui
from recipeWindowGUI import Ui_Form
import urllib.request
import api_functions as api
import user

class RecipeWindow():
    def __init__(self, window, id, is_logged, username, meals=None, names=None, ids=None):
        self.ui = Ui_Form()
        self.ui.setupUi(window)
        self.full_meals = meals
        self.only_names = names
        self.only_ids = ids
        self.id = id
        self.is_logged = is_logged
        self.username = username
        self.fav_icon = QtGui.QIcon()
        self.fav_icon.addPixmap(QtGui.QPixmap("fav.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.not_fav_icon = QtGui.QIcon()
        self.not_fav_icon.addPixmap(QtGui.QPixmap("notfav.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_buttons()


    def update_buttons(self):
        self.ui.next_pushButton.clicked.connect(self.next_recipe)
        self.ui.previous_pushButton.clicked.connect(self.prev_recipe)
        self.ui.fav_button.clicked.connect(self.fav)
        try:
            if self.is_logged:
                self.ui.fav_button.show()
            else:
                self.ui.fav_button.hide()
        except Exception as e:
            print(e)

    def next_recipe(self):
        self.id += 1
        self.load_recipe()

    def prev_recipe(self):
        self.id -= 1
        self.load_recipe()

    def fav(self):
        self.ui.fav_button.setIcon(self.fav_icon)
        user.add_to_fav(self.username, self.meal['id'])
        self.ui.fav_button.clicked.connect(self.unfav)


    def unfav(self):
        self.ui.fav_button.setIcon(self.not_fav_icon)
        user.remove_from_fav(self.username, self.meal['id'])
        self.ui.fav_button.clicked.connect(self.fav)

    def load_recipe(self):
        if self.full_meals:
            self.meal = self.full_meals[self.id]
        elif self.only_names:
            self.meal = api.get_meal(self.only_names[self.id]['idMeal'])[0]
        elif self.only_ids:
            self.meal = api.get_meal(self.only_ids[self.id])[0]

        self.ui.title_label.setText(self.meal['name'])
        self.ui.title_label.repaint()

        self.ui.category_label.setText(self.meal['category'])
        self.ui.cuisine_label.setText(self.meal['cuisine'])
        self.ui.ingredients.clear()
        for ing in self.meal['ingredients']:
            self.ui.ingredients.addItem(ing)
        self.ui.instructions.setText(self.meal['instructions'])
        self.ui.next_pushButton.hide()
        self.ui.previous_pushButton.hide()

        url = self.meal['image']
        data = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        pixmap = QtGui.QPixmap(image)
        self.ui.photo_label.setPixmap(pixmap.scaledToHeight(400))

        if (self.full_meals and len(self.full_meals)-1 > self.id) or (self.only_names and len(self.only_names)-1 > self.id) or (self.only_ids and len(self.only_ids)-1 > self.id):
            self.ui.next_pushButton.show()
        if self.id != 0:
            self.ui.previous_pushButton.show()

        if self.is_logged:
            if user.is_fav(self.username, self.meal['id']):
                self.ui.fav_button.setIcon(self.fav_icon)
                self.ui.fav_button.clicked.connect(self.unfav)
            else:
                self.ui.fav_button.setIcon(self.not_fav_icon)
                self.ui.fav_button.clicked.connect(self.fav)
