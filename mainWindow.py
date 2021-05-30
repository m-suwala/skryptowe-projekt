from PyQt5 import QtWidgets
import sys
import api_functions as api
from mainWindowGUI import Ui_MainWindow
from recipeWindow import RecipeWindow
from CuisinesList import Ui_Cuisines
from CategoriesList import Ui_Categories
from IngredientsList import Ui_Ingredients


class MainWindow():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.update_buttons()
        sys.exit(app.exec_())

    def update_buttons(self):
        self.ui.random_pushButton.clicked.connect(self.open_random_recipe)
        self.ui.categories_pushButton.clicked.connect(self.open_categories)
        self.ui.cuisines_pushButton.clicked.connect(self.open_cuisines)
        self.ui.ingredients_pushButton.clicked.connect(self.open_ingredients)
        self.ui.login_pushButton.clicked.connect(self.log_in)
        self.ui.new_pushButton.clicked.connect(self.create_acc)
        self.ui.search_lineEdit.returnPressed.connect(self.search)


    def open_random_recipe(self):
        self.window = QtWidgets.QMainWindow()
        self.recipe = RecipeWindow(self.window, api.get_random_meal(), 0, is_meal=True)
        self.recipe.load_recipe()
        self.window.show()


    def open_categories(self):
        self.Category = QtWidgets.QWidget()
        self.ui = Ui_Categories()
        self.ui.setupUi(self.Category)
        self.Category.show()


    def open_cuisines(self):
        self.Cuisines = QtWidgets.QWidget()
        self.ui = Ui_Cuisines()
        self.ui.setupUi(self.Cuisines)
        self.Cuisines.show()

    def open_ingredients(self):
        self.Ingredients = QtWidgets.QWidget()
        self.ui = Ui_Ingredients()
        self.ui.setupUi(self.Ingredients)
        self.Ingredients.show()

    def search(self):
        self.ui.error_label.hide()
        self.window = QtWidgets.QMainWindow()
        meals = api.get_meals(self.ui.search_lineEdit.text())
        if meals:
            self.recipe = RecipeWindow(self.window, meals, 0, is_meal=True)
            self.recipe.load_recipe()
            self.window.show()
            self.ui.search_lineEdit.clear()
        else:
            self.ui.error_label.setText("recipes not found")
            self.ui.error_label.show()

    def log_in(self):
        print("login")

    def create_acc(self):
        print("new acc")


if __name__ == "__main__":
    MainWindow()
