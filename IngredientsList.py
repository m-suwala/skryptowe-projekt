from PyQt5 import QtCore, QtGui, QtWidgets
import api_functions as api
from recipeWindow import RecipeWindow


class Ui_Ingredients(object):
    def setupUi(self, Ingredients):
        Ingredients.setObjectName("Ingredients")
        Ingredients.resize(400, 600)
        Ingredients.setStyleSheet("background-color: rgb(212, 237, 255);\n"
"color: rgb(25, 68, 124);")
        self.ingredients_list = QtWidgets.QListWidget(Ingredients)
        self.ingredients_list.setGeometry(QtCore.QRect(20, 101, 355, 471))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ingredients_list.setFont(font)
        self.ingredients_list.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.511, stop:0 rgb(239, 250, 255), stop:1 rgb(243, 247, 255));\n"
            "border: 1px solid rgb(69, 111, 179);\n"
            "border-radius: 5px;")
        self.ingredients_list.setObjectName("ingredients_list")
        self.ingredients_label = QtWidgets.QLabel(Ingredients)
        self.ingredients_label.setGeometry(QtCore.QRect(10, 19, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.ingredients_label.setFont(font)
        self.ingredients_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ingredients_label.setObjectName("ingredients_label")
        self.error_label = QtWidgets.QLabel(Ingredients)
        self.error_label.setGeometry(QtCore.QRect(30, 69, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.error_label.setFont(font)
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.error_label.hide()

        ingredients = api.get_list_of_ingredients()

        ingredients = sorted(ingredients, key=lambda i: i['strIngredient'])

        for ingredient in ingredients:
            self.ingredients_list.addItem(ingredient['strIngredient'])

        self.ingredients_list.clicked.connect(self.open_recipes)

        self.retranslateUi(Ingredients)
        QtCore.QMetaObject.connectSlotsByName(Ingredients)

    def open_recipes(self):
        self.error_label.hide()
        ingredient = self.ingredients_list.currentItem()
        meals = api.get_meals_by_ingredient(ingredient.text())
        if meals:
            self.window = QtWidgets.QMainWindow()
            self.recipe = RecipeWindow(self.window, meals, 0, is_meal=False)
            self.recipe.load_recipe()
            self.window.show()
        else:
            self.error_label.show()

    def retranslateUi(self, Ingredients):
        _translate = QtCore.QCoreApplication.translate
        Ingredients.setWindowTitle(_translate("Ingredients", "Ingredients"))
        self.ingredients_label.setText(_translate("Ingredients", "Ingredients:"))
        self.error_label.setText(_translate("Ingredients", "no recipes found"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ingredients = QtWidgets.QWidget()
    ui = Ui_Ingredients()
    ui.setupUi(Ingredients)
    Ingredients.show()
    sys.exit(app.exec_())
