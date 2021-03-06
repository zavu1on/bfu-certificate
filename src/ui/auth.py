from PyQt5 import QtCore, QtGui, QtWidgets
from src.manager.screen import ScreenManager
from src.manager.data import DataManager
from src.ui.certificate_list import CertificateListScreen


class AuthScreen(QtWidgets.QWidget):
    """ Экран авторизации пользователя """

    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(972, 531)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 971, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 170, 971, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setItalic(True)
        self.login.setFont(font)
        self.login.setStyleSheet("QLineEdit {\n"
                                 "    width: 200px;\n"
                                 "    border-radius: 8px;\n"
                                 "    padding: 0 2.5px;\n"
                                 "    outline: none;\n"
                                 "    border: 1px solid rgb(183, 183, 183);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    border-color: rgb(146, 146, 146);\n"
                                 "}")
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login, 0, QtCore.Qt.AlignHCenter)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setItalic(False)
        self.password.setFont(font)
        self.password.setStyleSheet("QLineEdit {\n"
                                    "    width: 200px;\n"
                                    "    border-radius: 8px;\n"
                                    "    padding: 0 2.5px;\n"
                                    "    outline: none;\n"
                                    "    border: 1px solid rgb(183, 183, 183);\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:hover {\n"
                                    "    border-color: rgb(146, 146, 146);\n"
                                    "}")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.password, 0, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    background: #2BBBAD;\n"
                                      "    color: #fff;\n"
                                      "    width: 100px;\n"
                                      "    border-radius: 6px;\n"
                                      "    padding: 4px\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background: #26ad9f;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Печать справок для БФУ имени Канта"))
        self.label.setText(_translate("MainWindow", "Авторизация"))
        self.login.setPlaceholderText(_translate("MainWindow", "Логин:"))
        self.password.setPlaceholderText(_translate("MainWindow", "Пароль:"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))

        QtCore.QMetaObject.connectSlotsByName(self)

        self.init_logic()

    def init_logic(self):
        """ Бизнес-логика для экрана авторизации """
        self.pushButton.clicked.connect(self.btn_click_handler)

    def btn_click_handler(self):
        """ Обработчик кнопки входа """
        input_login, input_password = self.login.text(), self.password.text()

        for login, password in DataManager().authentication_list:
            if input_login == login and input_password == password:
                ScreenManager.set_screen(CertificateListScreen(ScreenManager.get_ui()), self)
                return

        error_message = QtWidgets.QMessageBox(self)  # всплывающие окно об ошибке
        error_message.setWindowTitle('Ошибка авторизации')
        error_message.setText('Логин или пароль неверный')
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        error_message.setFont(font)
        error_message.exec_()
