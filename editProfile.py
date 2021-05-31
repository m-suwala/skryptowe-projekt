from PyQt5 import QtCore, QtGui, QtWidgets
import user


class Ui_Form(object):
    def setupUi(self, Form, username):
        self.username = username
        Form.setObjectName("Form")
        Form.resize(400, 434)
        Form.setStyleSheet("background-color: rgb(212, 237, 255);\n"
                           "color: rgb(25, 68, 124);\n"
                           "")
        self.current_pass = QtWidgets.QLineEdit(Form)
        self.current_pass.setGeometry(QtCore.QRect(40, 60, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_pass.sizePolicy().hasHeightForWidth())
        self.current_pass.setSizePolicy(sizePolicy)
        self.current_pass.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.current_pass.setFont(font)
        self.current_pass.setToolTipDuration(0)
        self.current_pass.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.current_pass.setAutoFillBackground(False)
        self.current_pass.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.511, stop:0 rgb(239, 250, 255), stop:1 rgb(243, 247, 255));\n"
                "border: 1px solid rgb(69, 111, 179);\n"
                "border-radius: 5px;\n"
                "\n"
                "\n"
                "")
        self.current_pass.setText("")
        self.current_pass.setFrame(False)
        self.current_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.current_pass.setCursorPosition(0)
        self.current_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.current_pass.setDragEnabled(False)
        self.current_pass.setClearButtonEnabled(True)
        self.current_pass.setObjectName("current_pass")
        self.change_pass_button = QtWidgets.QPushButton(Form)
        self.change_pass_button.setGeometry(QtCore.QRect(40, 140, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.change_pass_button.setFont(font)
        self.change_pass_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_pass_button.setAcceptDrops(False)
        self.change_pass_button.setStyleSheet("border-radius: 5px;\n"
                                              "background-color: rgb(141, 182, 217);\n"
                                              "color: rgb(237, 252, 255)")
        self.change_pass_button.setAutoRepeat(False)
        self.change_pass_button.setAutoDefault(False)
        self.change_pass_button.setDefault(False)
        self.change_pass_button.setFlat(False)
        self.change_pass_button.setObjectName("change_pass_button")
        self.new_pass = QtWidgets.QLineEdit(Form)
        self.new_pass.setGeometry(QtCore.QRect(40, 100, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_pass.sizePolicy().hasHeightForWidth())
        self.new_pass.setSizePolicy(sizePolicy)
        self.new_pass.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.new_pass.setFont(font)
        self.new_pass.setToolTipDuration(0)
        self.new_pass.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.new_pass.setAutoFillBackground(False)
        self.new_pass.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.511, stop:0 rgb(239, 250, 255), stop:1 rgb(243, 247, 255));\n"
                "border: 1px solid rgb(69, 111, 179);\n"
                "border-radius: 5px;\n"
                "\n"
                "\n"
                "")
        self.new_pass.setText("")
        self.new_pass.setFrame(False)
        self.new_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pass.setCursorPosition(0)
        self.new_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.new_pass.setDragEnabled(False)
        self.new_pass.setClearButtonEnabled(True)
        self.new_pass.setObjectName("new_pass")
        self.diet_list = QtWidgets.QComboBox(Form)
        self.diet_list.setGeometry(QtCore.QRect(40, 320, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.diet_list.setFont(font)
        self.diet_list.setObjectName("diet_list")
        self.diet_list.addItem("")
        self.diet_list.addItem("")
        self.diet_list.addItem("")
        self.choose_diet_button = QtWidgets.QPushButton(Form)
        self.choose_diet_button.setGeometry(QtCore.QRect(40, 360, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.choose_diet_button.setFont(font)
        self.choose_diet_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_diet_button.setAcceptDrops(False)
        self.choose_diet_button.setStyleSheet("border-radius: 5px;\n"
                                              "background-color: rgb(141, 182, 217);\n"
                                              "color: rgb(237, 252, 255)")
        self.choose_diet_button.setAutoRepeat(False)
        self.choose_diet_button.setAutoDefault(False)
        self.choose_diet_button.setDefault(False)
        self.choose_diet_button.setFlat(False)
        self.choose_diet_button.setObjectName("choose_diet_button")
        self.claer_fav_button = QtWidgets.QPushButton(Form)
        self.claer_fav_button.setGeometry(QtCore.QRect(40, 230, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.claer_fav_button.setFont(font)
        self.claer_fav_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.claer_fav_button.setAcceptDrops(False)
        self.claer_fav_button.setStyleSheet("border-radius: 5px;\n"
                                            "background-color: rgb(141, 182, 217);\n"
                                            "color: rgb(237, 252, 255)")
        self.claer_fav_button.setAutoRepeat(False)
        self.claer_fav_button.setAutoDefault(False)
        self.claer_fav_button.setDefault(False)
        self.claer_fav_button.setFlat(False)
        self.claer_fav_button.setObjectName("claer_fav_button")
        self.pass_change_info_label = QtWidgets.QLabel(Form)
        self.pass_change_info_label.setGeometry(QtCore.QRect(40, 170, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pass_change_info_label.sizePolicy().hasHeightForWidth())
        self.pass_change_info_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pass_change_info_label.setFont(font)
        self.pass_change_info_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pass_change_info_label.setScaledContents(True)
        self.pass_change_info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_change_info_label.setObjectName("pass_change_info_label")
        self.cleared_list_label = QtWidgets.QLabel(Form)
        self.cleared_list_label.setGeometry(QtCore.QRect(40, 260, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cleared_list_label.sizePolicy().hasHeightForWidth())
        self.cleared_list_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.cleared_list_label.setFont(font)
        self.cleared_list_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cleared_list_label.setScaledContents(True)
        self.cleared_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cleared_list_label.setObjectName("cleared_list_label")

        self.changed_diet_label = QtWidgets.QLabel(Form)
        self.changed_diet_label.setGeometry(QtCore.QRect(40, 390, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changed_diet_label.sizePolicy().hasHeightForWidth())
        self.changed_diet_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.changed_diet_label.setFont(font)
        self.changed_diet_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.changed_diet_label.setScaledContents(True)
        self.changed_diet_label.setAlignment(QtCore.Qt.AlignCenter)

        self.changed_diet_label.setObjectName("changed_diet_label")
        self.changed_diet_label.raise_()
        self.cleared_list_label.raise_()
        self.pass_change_info_label.raise_()
        self.current_pass.raise_()
        self.change_pass_button.raise_()
        self.new_pass.raise_()
        self.diet_list.raise_()
        self.choose_diet_button.raise_()
        self.claer_fav_button.raise_()

        self.change_pass_button.clicked.connect(self.change)
        self.pass_change_info_label.hide()

        self.cleared_list_label.hide()
        self.changed_diet_label.hide()

        self.claer_fav_button.clicked.connect(self.clear_fav)

        self.choose_diet_button.clicked.connect(self.choose_diet)

        diets = ["None", "Vegan", "Vegetarian"]
        self.diet_list.clear()
        self.diet_list.addItems(diets)
        diet = user.get_diet(self.username)
        self.diet_list.setCurrentText(diet)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def change(self):
        self.cleared_list_label.hide()
        self.changed_diet_label.hide()
        self.pass_change_info_label.hide()
        current_pass = self.current_pass.text()
        new_pass = self.new_pass.text()
        if len(new_pass) < 8:
            self.pass_change_info_label.setText("New password is too short")
            self.pass_change_info_label.show()
        else:
            if user.change_password(self.username, current_pass, new_pass):
                self.pass_change_info_label.setText("Password has been changed")
                self.pass_change_info_label.show()
            else:
                self.pass_change_info_label.setText("Wrong password")
                self.pass_change_info_label.show()

    def clear_fav(self):
        self.cleared_list_label.hide()
        self.changed_diet_label.hide()
        self.pass_change_info_label.hide()
        user.clear_fav(self.username)
        self.cleared_list_label.show()


    def choose_diet(self):
        new_diet = self.diet_list.currentText()
        user.change_diet(self.username, new_diet)
        self.changed_diet_label.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Edit profile"))
        self.current_pass.setPlaceholderText(_translate("Form", "Current password"))
        self.change_pass_button.setText(_translate("Form", "Change password"))
        self.new_pass.setPlaceholderText(_translate("Form", "New password"))
        self.diet_list.setItemText(0, _translate("Form", "None"))
        self.diet_list.setItemText(1, _translate("Form", "Vegan"))
        self.diet_list.setItemText(2, _translate("Form", "Vegetarian"))
        self.choose_diet_button.setText(_translate("Form", "Choose diet"))
        self.claer_fav_button.setText(_translate("Form", "Clear favourite recipe list"))
        self.pass_change_info_label.setText(_translate("Form", "Password has been changed"))
        self.cleared_list_label.setText(_translate("Form", "List cleared"))
        self.changed_diet_label.setText(_translate("Form", "Diet changed"))

