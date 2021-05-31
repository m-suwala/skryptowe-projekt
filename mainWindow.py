from PyQt5 import QtWidgets
import sys
import api_functions as api
from mainWindowGUI import Ui_MainWindow
from recipeWindow import RecipeWindow
from CuisinesList import Ui_Cuisines
from CategoriesList import Ui_Categories
from IngredientsList import Ui_Ingredients
from editProfile import Ui_Form
import user
from mongoengine import *


class MainWindow():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.update_buttons()
        self.is_logged = False
        self.username = None
        sys.exit(app.exec_())

    def update_buttons(self):
        self.ui.random_pushButton.clicked.connect(self.open_random_recipe)
        self.ui.categories_pushButton.clicked.connect(self.open_categories)
        self.ui.cuisines_pushButton.clicked.connect(self.open_cuisines)
        self.ui.ingredients_pushButton.clicked.connect(self.open_ingredients)
        self.ui.login_pushButton.clicked.connect(self.log_in)
        self.ui.new_pushButton.clicked.connect(self.create_acc)
        self.ui.search_lineEdit.returnPressed.connect(self.search)
        self.ui.go_to_fav_button.pressed.connect(self.go_to_favs)
        self.ui.logout_button.pressed.connect(self.logout)
        self.ui.edit_profile_button.pressed.connect(self.edit)

        self.ui.go_to_fav_button.hide()
        self.ui.welcome_label.hide()
        self.ui.logout_button.hide()
        self.ui.faverror_label.hide()
        self.ui.edit_profile_button.hide()

    def hide_errors(self):
        self.ui.faverror_label.hide()
        self.ui.error_label.hide()
        self.ui.loginerror_label.hide()
        self.ui.faverror_label.hide()

    def open_random_recipe(self):
        try:
            self.hide_errors()
            self.window = QtWidgets.QMainWindow()
            if not self.is_logged or user.get_diet(self.username) == "None":
                self.recipe = RecipeWindow(self.window, 0, is_logged=self.is_logged, username=self.username, meals=api.get_random_meal())
            else:
                self.recipe = RecipeWindow(self.window, 0, is_logged=self.is_logged, username=self.username, names=api.get_random_meal_diet(user.get_diet(self.username)))
            self.recipe.load_recipe()
            self.window.show()
        except Exception as e:
            print(e)

    def open_categories(self):
        self.hide_errors()
        self.Category = QtWidgets.QWidget()
        self.category = Ui_Categories()
        self.category.setupUi(self.Category, self.is_logged, username=self.username)
        self.Category.show()

    def open_cuisines(self):
        self.hide_errors()
        self.Cuisines = QtWidgets.QWidget()
        self.cuisine = Ui_Cuisines()
        self.cuisine.setupUi(self.Cuisines, self.is_logged, username=self.username)
        self.Cuisines.show()

    def open_ingredients(self):
        self.hide_errors()
        self.Ingredients = QtWidgets.QWidget()
        self.ingredient = Ui_Ingredients()
        self.ingredient.setupUi(self.Ingredients, self.is_logged, username=self.username)
        self.Ingredients.show()

    def search(self):
        self.hide_errors()
        try:
            self.window = QtWidgets.QMainWindow()
            name = self.ui.search_lineEdit.text()
            if name != "" and name != " ":
                meals = api.get_meals(name)
                if meals:
                    self.recipe = RecipeWindow(self.window, 0, is_logged=self.is_logged, username=self.username, meals=meals)
                    self.recipe.load_recipe()
                    self.window.show()
                    self.ui.search_lineEdit.clear()
                else:
                    self.ui.error_label.setText("Recipes not found")
                    self.ui.error_label.show()
        except Exception as e:
            print(e)

    def log_in(self):
        self.hide_errors()
        login = self.ui.login_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        log = user.login(login, password)
        if log:
            self.is_logged = True
            self.username = login
            self.logged_view()

        else:
            self.ui.loginerror_label.setText("Wrong login or password")
            self.ui.loginerror_label.show()

    def logged_view(self):
        self.ui.go_to_fav_button.show()
        self.ui.welcome_label.setText("Welcome " + self.username + "!")
        self.ui.welcome_label.show()
        self.ui.logout_button.show()
        self.ui.edit_profile_button.show()

        self.ui.login_lineEdit.clear()
        self.ui.password_lineEdit.clear()
        self.ui.login_lineEdit.hide()
        self.ui.password_lineEdit.hide()
        self.ui.login_pushButton.hide()
        self.ui.new_pushButton.hide()
        self.ui.or_label.hide()

    def not_logged_view(self):
        self.ui.login_lineEdit.show()
        self.ui.password_lineEdit.show()
        self.ui.login_pushButton.show()
        self.ui.new_pushButton.show()
        self.ui.or_label.show()

        self.ui.go_to_fav_button.hide()
        self.ui.welcome_label.hide()
        self.ui.logout_button.hide()
        self.ui.faverror_label.hide()
        self.ui.edit_profile_button.hide()

    def create_acc(self):
        self.hide_errors()
        login = self.ui.login_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        if login == "" or password == "":
            self.ui.loginerror_label.setText("Please enter login and password")
            self.ui.loginerror_label.show()
        else:
            try:
                user.create_acc(login, password)
                self.is_logged = True
                self.username = login
                self.logged_view()

            except ValidationError:
                self.ui.loginerror_label.setText("Password is too short")
                self.ui.loginerror_label.show()
            except NotUniqueError:
                self.ui.loginerror_label.setText("This login is already taken")
                self.ui.loginerror_label.show()
            except Exception as e:
                print(e)
                self.ui.loginerror_label.setText("Error, please try again")
                self.ui.loginerror_label.show()

    def go_to_favs(self):
        self.hide_errors()
        try:
            self.window = QtWidgets.QMainWindow()
            fav_ids = user.get_favs(self.username)
            if fav_ids:
                self.recipe = RecipeWindow(self.window, 0, is_logged=True, username=self.username, ids=fav_ids)
                self.recipe.load_recipe()
                self.window.show()
            else:
                self.ui.faverror_label.setText("No favourite recipes found")
                self.ui.faverror_label.show()
        except Exception:
            pass

    def logout(self):
        self.hide_errors()
        self.is_logged = False
        self.username = None
        self.not_logged_view()

    def edit(self):
        self.hide_errors()
        self.Edit = QtWidgets.QWidget()
        self.edit = Ui_Form()
        self.edit.setupUi(self.Edit, self.username)
        self.Edit.show()


if __name__ == "__main__":
    MainWindow()
