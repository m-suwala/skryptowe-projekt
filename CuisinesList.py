from PyQt5 import QtCore, QtGui, QtWidgets
import api_functions as api
from recipeWindow import RecipeWindow


class Ui_Cuisines(object):
    def setupUi(self, Cuisines, is_logged, username):
        self.is_logged = is_logged
        self.username = username
        Cuisines.setObjectName("Cuisines")
        Cuisines.resize(400, 600)
        Cuisines.setStyleSheet("background-color: rgb(212, 237, 255);\n"
"color: rgb(25, 68, 124);")
        self.cuisines_list = QtWidgets.QListWidget(Cuisines)
        self.cuisines_list.setGeometry(QtCore.QRect(30, 101, 341, 471))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cuisines_list.setFont(font)
        self.cuisines_list.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.511, stop:0 rgb(239, 250, 255), stop:1 rgb(243, 247, 255));\n"
            "border: 1px solid rgb(69, 111, 179);\n"
            "border-radius: 5px;")
        self.cuisines_list.setObjectName("cuisines_list")
        self.cuisines_label = QtWidgets.QLabel(Cuisines)
        self.cuisines_label.setGeometry(QtCore.QRect(10, 19, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(20)
        self.cuisines_label.setFont(font)
        self.cuisines_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cuisines_label.setObjectName("cuisines_label")

        cuisines = api.get_list_of_cuisines()

        for cuisine in cuisines:
            self.cuisines_list.addItem(cuisine['strArea'])

        self.cuisines_list.clicked.connect(self.open_recipes)

        self.retranslateUi(Cuisines)
        QtCore.QMetaObject.connectSlotsByName(Cuisines)


    def open_recipes(self):
        cuisine = self.cuisines_list.currentItem()
        meals = api.get_meals_by_cuisine(cuisine.text())
        self.window = QtWidgets.QMainWindow()
        self.recipe = RecipeWindow(self.window, 0, is_logged=self.is_logged, username=self.username, names=meals)
        self.recipe.load_recipe()
        self.window.show()


    def retranslateUi(self, Cuisines):
        _translate = QtCore.QCoreApplication.translate
        Cuisines.setWindowTitle(_translate("Cuisines", "Cuisines"))
        self.cuisines_label.setText(_translate("Cuisines", "Cuisines:"))
