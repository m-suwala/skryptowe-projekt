from PyQt5 import QtCore, QtGui, QtWidgets
import api_functions as api
from recipeWindow import RecipeWindow

class Ui_Categories(object):
    def setupUi(self, Categories):
        Categories.setObjectName("Categories")
        Categories.resize(400, 600)
        Categories.setStyleSheet("background-color: rgb(212, 237, 255);\n"
"color: rgb(25, 68, 124);")
        self.categories_list = QtWidgets.QListWidget(Categories)
        self.categories_list.setGeometry(QtCore.QRect(30, 101, 341, 471))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.categories_list.setFont(font)
        self.categories_list.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.511, stop:0 rgb(239, 250, 255), stop:1 rgb(243, 247, 255));\n"
            "border: 1px solid rgb(69, 111, 179);\n"
            "border-radius: 5px;")
        self.categories_list.setObjectName("categories_list")
        self.categories_label = QtWidgets.QLabel(Categories)
        self.categories_label.setGeometry(QtCore.QRect(10, 19, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(20)
        self.categories_label.setFont(font)
        self.categories_label.setAlignment(QtCore.Qt.AlignCenter)
        self.categories_label.setObjectName("categories_label")

        categories = api.get_list_of_categories()

        for category in categories:
            self.categories_list.addItem(category['strCategory'])

        self.categories_list.clicked.connect(self.open_recipes)

        self.retranslateUi(Categories)
        QtCore.QMetaObject.connectSlotsByName(Categories)

    def open_recipes(self):
        category = self.categories_list.currentItem()
        meals = api.get_meals_by_category(category.text())
        self.window = QtWidgets.QMainWindow()
        self.recipe = RecipeWindow(self.window, meals, 0, is_meal=False)
        self.recipe.load_recipe()
        self.window.show()

    def retranslateUi(self, Categories):
        _translate = QtCore.QCoreApplication.translate
        Categories.setWindowTitle(_translate("Categories", "Categories"))
        self.categories_label.setText(_translate("Categories", "Categories:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Categories = QtWidgets.QWidget()
    ui = Ui_Categories()
    ui.setupUi(Categories)
    Categories.show()
    sys.exit(app.exec_())
