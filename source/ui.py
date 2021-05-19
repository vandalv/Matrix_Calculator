from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1124, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1124, 600))
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("\n"
"background-color: #37363f;\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.matrixA_00 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_00.setGeometry(QtCore.QRect(30, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_00.setFont(font)
        self.matrixA_00.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_00.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_00.setMaxLength(3)
        self.matrixA_00.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_00.setObjectName("matrixA_00")
        self.matrixA_01 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_01.setGeometry(QtCore.QRect(90, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_01.setFont(font)
        self.matrixA_01.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_01.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_01.setMaxLength(3)
        self.matrixA_01.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_01.setObjectName("matrixA_01")
        self.matrixA_02 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_02.setGeometry(QtCore.QRect(150, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_02.setFont(font)
        self.matrixA_02.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_02.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_02.setMaxLength(3)
        self.matrixA_02.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_02.setObjectName("matrixA_02")
        self.matrixA_03 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_03.setGeometry(QtCore.QRect(210, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_03.setFont(font)
        self.matrixA_03.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_03.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_03.setText("")
        self.matrixA_03.setMaxLength(3)
        self.matrixA_03.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_03.setObjectName("matrixA_03")
        self.matrixA_04 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_04.setGeometry(QtCore.QRect(270, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_04.setFont(font)
        self.matrixA_04.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_04.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_04.setText("")
        self.matrixA_04.setMaxLength(3)
        self.matrixA_04.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_04.setObjectName("matrixA_04")
        self.matrixA_08 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_08.setGeometry(QtCore.QRect(210, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_08.setFont(font)
        self.matrixA_08.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_08.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_08.setText("")
        self.matrixA_08.setMaxLength(3)
        self.matrixA_08.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_08.setObjectName("matrixA_08")
        self.matrixA_09 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_09.setGeometry(QtCore.QRect(270, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_09.setFont(font)
        self.matrixA_09.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_09.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_09.setText("")
        self.matrixA_09.setMaxLength(3)
        self.matrixA_09.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_09.setObjectName("matrixA_09")
        self.matrixA_07 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_07.setGeometry(QtCore.QRect(150, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_07.setFont(font)
        self.matrixA_07.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_07.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_07.setMaxLength(3)
        self.matrixA_07.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_07.setObjectName("matrixA_07")
        self.matrixA_06 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_06.setGeometry(QtCore.QRect(90, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_06.setFont(font)
        self.matrixA_06.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_06.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_06.setMaxLength(3)
        self.matrixA_06.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_06.setObjectName("matrixA_06")
        self.matrixA_05 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_05.setGeometry(QtCore.QRect(30, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_05.setFont(font)
        self.matrixA_05.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_05.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_05.setMaxLength(3)
        self.matrixA_05.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_05.setObjectName("matrixA_05")
        self.matrixA_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_13.setGeometry(QtCore.QRect(210, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_13.setFont(font)
        self.matrixA_13.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_13.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_13.setText("")
        self.matrixA_13.setMaxLength(3)
        self.matrixA_13.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_13.setObjectName("matrixA_13")
        self.matrixA_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_14.setGeometry(QtCore.QRect(270, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_14.setFont(font)
        self.matrixA_14.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_14.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_14.setText("")
        self.matrixA_14.setMaxLength(3)
        self.matrixA_14.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_14.setObjectName("matrixA_14")
        self.matrixA_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_12.setGeometry(QtCore.QRect(150, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_12.setFont(font)
        self.matrixA_12.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_12.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_12.setMaxLength(3)
        self.matrixA_12.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_12.setObjectName("matrixA_12")
        self.matrixA_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_11.setGeometry(QtCore.QRect(90, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_11.setFont(font)
        self.matrixA_11.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_11.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_11.setMaxLength(3)
        self.matrixA_11.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_11.setObjectName("matrixA_11")
        self.matrixA_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_10.setGeometry(QtCore.QRect(30, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_10.setFont(font)
        self.matrixA_10.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_10.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_10.setMaxLength(3)
        self.matrixA_10.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_10.setObjectName("matrixA_10")
        self.matrixA_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_18.setGeometry(QtCore.QRect(210, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_18.setFont(font)
        self.matrixA_18.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_18.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_18.setText("")
        self.matrixA_18.setMaxLength(3)
        self.matrixA_18.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_18.setObjectName("matrixA_18")
        self.matrixA_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_19.setGeometry(QtCore.QRect(270, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_19.setFont(font)
        self.matrixA_19.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_19.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_19.setText("")
        self.matrixA_19.setMaxLength(3)
        self.matrixA_19.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_19.setObjectName("matrixA_19")
        self.matrixA_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_17.setGeometry(QtCore.QRect(150, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_17.setFont(font)
        self.matrixA_17.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_17.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_17.setText("")
        self.matrixA_17.setMaxLength(3)
        self.matrixA_17.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_17.setObjectName("matrixA_17")
        self.matrixA_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_16.setGeometry(QtCore.QRect(90, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_16.setFont(font)
        self.matrixA_16.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_16.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_16.setText("")
        self.matrixA_16.setMaxLength(3)
        self.matrixA_16.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_16.setObjectName("matrixA_16")
        self.matrixA_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_15.setGeometry(QtCore.QRect(30, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_15.setFont(font)
        self.matrixA_15.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_15.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_15.setText("")
        self.matrixA_15.setMaxLength(3)
        self.matrixA_15.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_15.setObjectName("matrixA_15")
        self.matrixA_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_23.setGeometry(QtCore.QRect(210, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_23.setFont(font)
        self.matrixA_23.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_23.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_23.setText("")
        self.matrixA_23.setMaxLength(3)
        self.matrixA_23.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_23.setObjectName("matrixA_23")
        self.matrixA_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_24.setGeometry(QtCore.QRect(270, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_24.setFont(font)
        self.matrixA_24.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_24.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_24.setText("")
        self.matrixA_24.setMaxLength(3)
        self.matrixA_24.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_24.setObjectName("matrixA_24")
        self.matrixA_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_22.setGeometry(QtCore.QRect(150, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_22.setFont(font)
        self.matrixA_22.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_22.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_22.setText("")
        self.matrixA_22.setMaxLength(3)
        self.matrixA_22.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_22.setObjectName("matrixA_22")
        self.matrixA_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_21.setGeometry(QtCore.QRect(90, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_21.setFont(font)
        self.matrixA_21.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_21.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_21.setText("")
        self.matrixA_21.setMaxLength(3)
        self.matrixA_21.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_21.setObjectName("matrixA_21")
        self.matrixA_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixA_20.setGeometry(QtCore.QRect(30, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixA_20.setFont(font)
        self.matrixA_20.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixA_20.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixA_20.setText("")
        self.matrixA_20.setMaxLength(3)
        self.matrixA_20.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA_20.setObjectName("matrixA_20")
        self.matrixC_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_22.setGeometry(QtCore.QRect(930, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_22.setFont(font)
        self.matrixC_22.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_22.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_22.setText("")
        self.matrixC_22.setMaxLength(3)
        self.matrixC_22.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_22.setObjectName("matrixC_22")
        self.matrixC_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_15.setGeometry(QtCore.QRect(810, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_15.setFont(font)
        self.matrixC_15.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_15.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_15.setText("")
        self.matrixC_15.setMaxLength(3)
        self.matrixC_15.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_15.setObjectName("matrixC_15")
        self.matrixC_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_20.setGeometry(QtCore.QRect(810, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_20.setFont(font)
        self.matrixC_20.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_20.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_20.setText("")
        self.matrixC_20.setMaxLength(3)
        self.matrixC_20.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_20.setObjectName("matrixC_20")
        self.matrixC_06 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_06.setGeometry(QtCore.QRect(870, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_06.setFont(font)
        self.matrixC_06.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_06.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_06.setText("")
        self.matrixC_06.setMaxLength(3)
        self.matrixC_06.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_06.setObjectName("matrixC_06")
        self.matrixC_03 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_03.setGeometry(QtCore.QRect(990, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_03.setFont(font)
        self.matrixC_03.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_03.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_03.setText("")
        self.matrixC_03.setMaxLength(3)
        self.matrixC_03.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_03.setObjectName("matrixC_03")
        self.matrixC_04 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_04.setGeometry(QtCore.QRect(1050, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_04.setFont(font)
        self.matrixC_04.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_04.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_04.setText("")
        self.matrixC_04.setMaxLength(3)
        self.matrixC_04.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_04.setObjectName("matrixC_04")
        self.matrixC_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_16.setGeometry(QtCore.QRect(870, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_16.setFont(font)
        self.matrixC_16.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_16.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_16.setText("")
        self.matrixC_16.setMaxLength(3)
        self.matrixC_16.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_16.setObjectName("matrixC_16")
        self.matrixC_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_11.setGeometry(QtCore.QRect(870, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_11.setFont(font)
        self.matrixC_11.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_11.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_11.setText("")
        self.matrixC_11.setMaxLength(3)
        self.matrixC_11.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_11.setObjectName("matrixC_11")
        self.matrixC_07 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_07.setGeometry(QtCore.QRect(930, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_07.setFont(font)
        self.matrixC_07.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_07.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_07.setText("")
        self.matrixC_07.setMaxLength(3)
        self.matrixC_07.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_07.setObjectName("matrixC_07")
        self.matrixC_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_12.setGeometry(QtCore.QRect(930, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_12.setFont(font)
        self.matrixC_12.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_12.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_12.setText("")
        self.matrixC_12.setMaxLength(3)
        self.matrixC_12.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_12.setObjectName("matrixC_12")
        self.matrixC_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_10.setGeometry(QtCore.QRect(810, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_10.setFont(font)
        self.matrixC_10.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_10.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_10.setText("")
        self.matrixC_10.setMaxLength(3)
        self.matrixC_10.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_10.setObjectName("matrixC_10")
        self.matrixC_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_18.setGeometry(QtCore.QRect(990, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_18.setFont(font)
        self.matrixC_18.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_18.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_18.setText("")
        self.matrixC_18.setMaxLength(3)
        self.matrixC_18.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_18.setObjectName("matrixC_18")
        self.matrixC_00 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_00.setGeometry(QtCore.QRect(810, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_00.setFont(font)
        self.matrixC_00.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_00.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_00.setText("")
        self.matrixC_00.setMaxLength(3)
        self.matrixC_00.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_00.setObjectName("matrixC_00")
        self.matrixC_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_14.setGeometry(QtCore.QRect(1050, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_14.setFont(font)
        self.matrixC_14.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_14.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_14.setText("")
        self.matrixC_14.setMaxLength(3)
        self.matrixC_14.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_14.setObjectName("matrixC_14")
        self.matrixC_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_19.setGeometry(QtCore.QRect(1050, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_19.setFont(font)
        self.matrixC_19.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_19.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_19.setText("")
        self.matrixC_19.setMaxLength(3)
        self.matrixC_19.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_19.setObjectName("matrixC_19")
        self.matrixC_01 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_01.setGeometry(QtCore.QRect(870, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_01.setFont(font)
        self.matrixC_01.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_01.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_01.setText("")
        self.matrixC_01.setMaxLength(3)
        self.matrixC_01.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_01.setObjectName("matrixC_01")
        self.matrixC_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_21.setGeometry(QtCore.QRect(870, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_21.setFont(font)
        self.matrixC_21.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_21.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_21.setText("")
        self.matrixC_21.setMaxLength(3)
        self.matrixC_21.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_21.setObjectName("matrixC_21")
        self.matrixC_05 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_05.setGeometry(QtCore.QRect(810, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_05.setFont(font)
        self.matrixC_05.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_05.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_05.setText("")
        self.matrixC_05.setMaxLength(3)
        self.matrixC_05.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_05.setObjectName("matrixC_05")
        self.matrixC_09 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_09.setGeometry(QtCore.QRect(1050, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_09.setFont(font)
        self.matrixC_09.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_09.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_09.setText("")
        self.matrixC_09.setMaxLength(3)
        self.matrixC_09.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_09.setObjectName("matrixC_09")
        self.matrixC_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_23.setGeometry(QtCore.QRect(990, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_23.setFont(font)
        self.matrixC_23.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_23.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_23.setText("")
        self.matrixC_23.setMaxLength(3)
        self.matrixC_23.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_23.setObjectName("matrixC_23")
        self.matrixC_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_24.setGeometry(QtCore.QRect(1050, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_24.setFont(font)
        self.matrixC_24.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_24.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_24.setText("")
        self.matrixC_24.setMaxLength(3)
        self.matrixC_24.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_24.setObjectName("matrixC_24")
        self.matrixC_08 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_08.setGeometry(QtCore.QRect(990, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_08.setFont(font)
        self.matrixC_08.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_08.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_08.setText("")
        self.matrixC_08.setMaxLength(3)
        self.matrixC_08.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_08.setObjectName("matrixC_08")
        self.matrixC_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_17.setGeometry(QtCore.QRect(930, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_17.setFont(font)
        self.matrixC_17.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_17.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_17.setText("")
        self.matrixC_17.setMaxLength(3)
        self.matrixC_17.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_17.setObjectName("matrixC_17")
        self.matrixC_02 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_02.setGeometry(QtCore.QRect(930, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_02.setFont(font)
        self.matrixC_02.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_02.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_02.setText("")
        self.matrixC_02.setMaxLength(3)
        self.matrixC_02.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_02.setObjectName("matrixC_02")
        self.matrixC_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixC_13.setGeometry(QtCore.QRect(990, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixC_13.setFont(font)
        self.matrixC_13.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixC_13.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixC_13.setText("")
        self.matrixC_13.setMaxLength(3)
        self.matrixC_13.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixC_13.setObjectName("matrixC_13")
        self.matrixB_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_22.setGeometry(QtCore.QRect(540, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_22.setFont(font)
        self.matrixB_22.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_22.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_22.setText("")
        self.matrixB_22.setMaxLength(3)
        self.matrixB_22.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_22.setObjectName("matrixB_22")
        self.matrixB_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_15.setGeometry(QtCore.QRect(420, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_15.setFont(font)
        self.matrixB_15.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_15.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_15.setText("")
        self.matrixB_15.setMaxLength(3)
        self.matrixB_15.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_15.setObjectName("matrixB_15")
        self.matrixB_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_20.setGeometry(QtCore.QRect(420, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_20.setFont(font)
        self.matrixB_20.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_20.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_20.setText("")
        self.matrixB_20.setMaxLength(3)
        self.matrixB_20.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_20.setObjectName("matrixB_20")
        self.matrixB_06 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_06.setGeometry(QtCore.QRect(480, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_06.setFont(font)
        self.matrixB_06.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_06.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_06.setMaxLength(3)
        self.matrixB_06.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_06.setObjectName("matrixB_06")
        self.matrixB_03 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_03.setGeometry(QtCore.QRect(600, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_03.setFont(font)
        self.matrixB_03.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_03.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_03.setText("")
        self.matrixB_03.setMaxLength(3)
        self.matrixB_03.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_03.setObjectName("matrixB_03")
        self.matrixB_04 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_04.setGeometry(QtCore.QRect(660, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_04.setFont(font)
        self.matrixB_04.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_04.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_04.setText("")
        self.matrixB_04.setMaxLength(3)
        self.matrixB_04.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_04.setObjectName("matrixB_04")
        self.matrixB_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_16.setGeometry(QtCore.QRect(480, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_16.setFont(font)
        self.matrixB_16.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_16.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_16.setText("")
        self.matrixB_16.setMaxLength(3)
        self.matrixB_16.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_16.setObjectName("matrixB_16")
        self.matrixB_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_11.setGeometry(QtCore.QRect(480, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_11.setFont(font)
        self.matrixB_11.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_11.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_11.setMaxLength(3)
        self.matrixB_11.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_11.setObjectName("matrixB_11")
        self.matrixB_07 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_07.setGeometry(QtCore.QRect(540, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_07.setFont(font)
        self.matrixB_07.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_07.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_07.setMaxLength(3)
        self.matrixB_07.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_07.setObjectName("matrixB_07")
        self.matrixB_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_12.setGeometry(QtCore.QRect(540, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_12.setFont(font)
        self.matrixB_12.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_12.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_12.setMaxLength(3)
        self.matrixB_12.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_12.setObjectName("matrixB_12")
        self.matrixB_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_10.setGeometry(QtCore.QRect(420, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_10.setFont(font)
        self.matrixB_10.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_10.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_10.setMaxLength(3)
        self.matrixB_10.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_10.setObjectName("matrixB_10")
        self.matrixB_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_18.setGeometry(QtCore.QRect(600, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_18.setFont(font)
        self.matrixB_18.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_18.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_18.setText("")
        self.matrixB_18.setMaxLength(3)
        self.matrixB_18.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_18.setObjectName("matrixB_18")
        self.matrixB_00 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_00.setGeometry(QtCore.QRect(420, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_00.setFont(font)
        self.matrixB_00.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_00.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_00.setMaxLength(3)
        self.matrixB_00.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_00.setObjectName("matrixB_00")
        self.matrixB_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_14.setGeometry(QtCore.QRect(660, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_14.setFont(font)
        self.matrixB_14.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_14.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_14.setText("")
        self.matrixB_14.setMaxLength(3)
        self.matrixB_14.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_14.setObjectName("matrixB_14")
        self.matrixB_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_19.setGeometry(QtCore.QRect(660, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_19.setFont(font)
        self.matrixB_19.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_19.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_19.setText("")
        self.matrixB_19.setMaxLength(3)
        self.matrixB_19.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_19.setObjectName("matrixB_19")
        self.matrixB_01 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_01.setGeometry(QtCore.QRect(480, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_01.setFont(font)
        self.matrixB_01.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_01.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_01.setMaxLength(3)
        self.matrixB_01.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_01.setObjectName("matrixB_01")
        self.matrixB_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_21.setGeometry(QtCore.QRect(480, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_21.setFont(font)
        self.matrixB_21.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_21.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_21.setText("")
        self.matrixB_21.setMaxLength(3)
        self.matrixB_21.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_21.setObjectName("matrixB_21")
        self.matrixB_05 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_05.setGeometry(QtCore.QRect(420, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_05.setFont(font)
        self.matrixB_05.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_05.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_05.setMaxLength(3)
        self.matrixB_05.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_05.setObjectName("matrixB_05")
        self.matrixB_09 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_09.setGeometry(QtCore.QRect(660, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_09.setFont(font)
        self.matrixB_09.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_09.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_09.setText("")
        self.matrixB_09.setMaxLength(3)
        self.matrixB_09.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_09.setObjectName("matrixB_09")
        self.matrixB_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_23.setGeometry(QtCore.QRect(600, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_23.setFont(font)
        self.matrixB_23.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_23.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_23.setText("")
        self.matrixB_23.setMaxLength(3)
        self.matrixB_23.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_23.setObjectName("matrixB_23")
        self.matrixB_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_24.setGeometry(QtCore.QRect(660, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_24.setFont(font)
        self.matrixB_24.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_24.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_24.setText("")
        self.matrixB_24.setMaxLength(3)
        self.matrixB_24.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_24.setObjectName("matrixB_24")
        self.matrixB_08 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_08.setGeometry(QtCore.QRect(600, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_08.setFont(font)
        self.matrixB_08.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_08.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_08.setText("")
        self.matrixB_08.setMaxLength(3)
        self.matrixB_08.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_08.setObjectName("matrixB_08")
        self.matrixB_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_17.setGeometry(QtCore.QRect(540, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_17.setFont(font)
        self.matrixB_17.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_17.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_17.setText("")
        self.matrixB_17.setMaxLength(3)
        self.matrixB_17.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_17.setObjectName("matrixB_17")
        self.matrixB_02 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_02.setGeometry(QtCore.QRect(540, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_02.setFont(font)
        self.matrixB_02.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_02.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_02.setMaxLength(3)
        self.matrixB_02.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_02.setObjectName("matrixB_02")
        self.matrixB_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.matrixB_13.setGeometry(QtCore.QRect(600, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.matrixB_13.setFont(font)
        self.matrixB_13.setStyleSheet("background-color: #36353d;\n"
"border: 2px solid #e05576;\n"
"border-radius: 7;\n"
"color: white;")
        self.matrixB_13.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.matrixB_13.setText("")
        self.matrixB_13.setMaxLength(3)
        self.matrixB_13.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB_13.setObjectName("matrixB_13")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1141, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources_rc/style_2.png"))
        self.label.setObjectName("label")
        self.pushButtonPlus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPlus.setGeometry(QtCore.QRect(340, 230, 51, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(25)
        self.pushButtonPlus.setFont(font)
        self.pushButtonPlus.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #59bbd7\n"
"    }")
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.pushButtonMinus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMinus.setGeometry(QtCore.QRect(340, 280, 51, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(25)
        self.pushButtonMinus.setFont(font)
        self.pushButtonMinus.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #59bbd7\n"
"    }")
        self.pushButtonMinus.setObjectName("pushButtonMinus")
        self.pushButtonMultiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMultiply.setGeometry(QtCore.QRect(340, 330, 51, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(14)
        self.pushButtonMultiply.setFont(font)
        self.pushButtonMultiply.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #59bbd7\n"
"    }")
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.pushButtonEqual = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEqual.setGeometry(QtCore.QRect(730, 280, 51, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(19)
        self.pushButtonEqual.setFont(font)
        self.pushButtonEqual.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"")
        self.pushButtonEqual.setObjectName("pushButtonEqual")
        self.pushButtonDetA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDetA.setGeometry(QtCore.QRect(30, 440, 71, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(14)
        font.setUnderline(False)
        self.pushButtonDetA.setFont(font)
        self.pushButtonDetA.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #59bbd7\n"
"    }")
        self.pushButtonDetA.setObjectName("pushButtonDetA")
        self.textLabel = QtWidgets.QLabel(self.centralwidget)
        self.textLabel.setGeometry(QtCore.QRect(330, 520, 461, 21))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(22)
        self.textLabel.setFont(font)
        self.textLabel.setStyleSheet("background-color: #d7596b;\n"
"color: white;")
        self.textLabel.setObjectName("textLabel")
        self.pushButtonTransposeA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonTransposeA.setGeometry(QtCore.QRect(130, 440, 91, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(14)
        font.setUnderline(False)
        self.pushButtonTransposeA.setFont(font)
        self.pushButtonTransposeA.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #59bbd7\n"
"    }")
        self.pushButtonTransposeA.setObjectName("pushButtonTransposeA")
        self.pushButtonDetB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDetB.setGeometry(QtCore.QRect(420, 440, 71, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(14)
        font.setUnderline(False)
        self.pushButtonDetB.setFont(font)
        self.pushButtonDetB.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #59bbd7\n"
"    }")
        self.pushButtonDetB.setObjectName("pushButtonDetB")
        self.pushButtonTransposeB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonTransposeB.setGeometry(QtCore.QRect(520, 440, 91, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(14)
        font.setUnderline(False)
        self.pushButtonTransposeB.setFont(font)
        self.pushButtonTransposeB.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #59bbd7\n"
"    }")
        self.pushButtonTransposeB.setObjectName("pushButtonTransposeB")
        self.pushButtonDetC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDetC.setGeometry(QtCore.QRect(810, 440, 71, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(14)
        font.setUnderline(False)
        self.pushButtonDetC.setFont(font)
        self.pushButtonDetC.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #59bbd7\n"
"    }")
        self.pushButtonDetC.setObjectName("pushButtonDetC")
        self.pushButtonTransposeC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonTransposeC.setGeometry(QtCore.QRect(910, 440, 91, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(14)
        font.setUnderline(False)
        self.pushButtonTransposeC.setFont(font)
        self.pushButtonTransposeC.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #59bbd7\n"
"    }")
        self.pushButtonTransposeC.setObjectName("pushButtonTransposeC")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-10, 90, 1131, 511))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("resources_rc/bg.png"))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 510, 521, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("resources_rc/tx_2.png"))
        self.label_2.setObjectName("label_2")
        self.pushButtonClearA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonClearA.setGeometry(QtCore.QRect(250, 440, 61, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(14)
        font.setUnderline(False)
        self.pushButtonClearA.setFont(font)
        self.pushButtonClearA.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #59bbd7\n"
"    }")
        self.pushButtonClearA.setObjectName("pushButtonClearA")
        self.pushButtonClearB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonClearB.setGeometry(QtCore.QRect(640, 440, 61, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(14)
        font.setUnderline(False)
        self.pushButtonClearB.setFont(font)
        self.pushButtonClearB.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #59bbd7\n"
"    }")
        self.pushButtonClearB.setObjectName("pushButtonClearB")
        self.pushButtonClearB_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonClearB_2.setGeometry(QtCore.QRect(1030, 440, 61, 31))
        font = QtGui.QFont()
        font.setFamily("College Condensed")
        font.setPointSize(14)
        font.setUnderline(False)
        self.pushButtonClearB_2.setFont(font)
        self.pushButtonClearB_2.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 2px solid #b34252;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: #d7596b;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ec4497\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #59bbd7\n"
"    }")
        self.pushButtonClearB_2.setObjectName("pushButtonClearB_2")
        self.label_3.raise_()
        self.label_2.raise_()
        self.matrixA_00.raise_()
        self.matrixA_01.raise_()
        self.matrixA_02.raise_()
        self.matrixA_03.raise_()
        self.matrixA_04.raise_()
        self.matrixA_08.raise_()
        self.matrixA_09.raise_()
        self.matrixA_07.raise_()
        self.matrixA_06.raise_()
        self.matrixA_05.raise_()
        self.matrixA_13.raise_()
        self.matrixA_14.raise_()
        self.matrixA_12.raise_()
        self.matrixA_11.raise_()
        self.matrixA_10.raise_()
        self.matrixA_18.raise_()
        self.matrixA_19.raise_()
        self.matrixA_17.raise_()
        self.matrixA_16.raise_()
        self.matrixA_15.raise_()
        self.matrixA_23.raise_()
        self.matrixA_24.raise_()
        self.matrixA_22.raise_()
        self.matrixA_21.raise_()
        self.matrixA_20.raise_()
        self.matrixC_22.raise_()
        self.matrixC_15.raise_()
        self.matrixC_20.raise_()
        self.matrixC_06.raise_()
        self.matrixC_03.raise_()
        self.matrixC_04.raise_()
        self.matrixC_16.raise_()
        self.matrixC_11.raise_()
        self.matrixC_07.raise_()
        self.matrixC_12.raise_()
        self.matrixC_10.raise_()
        self.matrixC_18.raise_()
        self.matrixC_00.raise_()
        self.matrixC_14.raise_()
        self.matrixC_19.raise_()
        self.matrixC_01.raise_()
        self.matrixC_21.raise_()
        self.matrixC_05.raise_()
        self.matrixC_09.raise_()
        self.matrixC_23.raise_()
        self.matrixC_24.raise_()
        self.matrixC_08.raise_()
        self.matrixC_17.raise_()
        self.matrixC_02.raise_()
        self.matrixC_13.raise_()
        self.matrixB_22.raise_()
        self.matrixB_15.raise_()
        self.matrixB_20.raise_()
        self.matrixB_06.raise_()
        self.matrixB_03.raise_()
        self.matrixB_04.raise_()
        self.matrixB_16.raise_()
        self.matrixB_11.raise_()
        self.matrixB_07.raise_()
        self.matrixB_12.raise_()
        self.matrixB_10.raise_()
        self.matrixB_18.raise_()
        self.matrixB_00.raise_()
        self.matrixB_14.raise_()
        self.matrixB_19.raise_()
        self.matrixB_01.raise_()
        self.matrixB_21.raise_()
        self.matrixB_05.raise_()
        self.matrixB_09.raise_()
        self.matrixB_23.raise_()
        self.matrixB_24.raise_()
        self.matrixB_08.raise_()
        self.matrixB_17.raise_()
        self.matrixB_02.raise_()
        self.matrixB_13.raise_()
        self.label.raise_()
        self.pushButtonPlus.raise_()
        self.pushButtonMinus.raise_()
        self.pushButtonMultiply.raise_()
        self.pushButtonEqual.raise_()
        self.pushButtonDetA.raise_()
        self.textLabel.raise_()
        self.pushButtonTransposeA.raise_()
        self.pushButtonDetB.raise_()
        self.pushButtonTransposeB.raise_()
        self.pushButtonDetC.raise_()
        self.pushButtonTransposeC.raise_()
        self.pushButtonClearA.raise_()
        self.pushButtonClearB.raise_()
        self.pushButtonClearB_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.matrixA_00.setText(_translate("MainWindow", "-3"))
        self.matrixA_01.setText(_translate("MainWindow", "12"))
        self.matrixA_02.setText(_translate("MainWindow", "74"))
        self.matrixA_07.setText(_translate("MainWindow", "55"))
        self.matrixA_06.setText(_translate("MainWindow", "23"))
        self.matrixA_05.setText(_translate("MainWindow", "12"))
        self.matrixA_12.setText(_translate("MainWindow", "4"))
        self.matrixA_11.setText(_translate("MainWindow", "43"))
        self.matrixA_10.setText(_translate("MainWindow", "-9"))
        self.matrixB_06.setText(_translate("MainWindow", "17"))
        self.matrixB_11.setText(_translate("MainWindow", "22"))
        self.matrixB_07.setText(_translate("MainWindow", "1"))
        self.matrixB_12.setText(_translate("MainWindow", "0"))
        self.matrixB_10.setText(_translate("MainWindow", "13"))
        self.matrixB_00.setText(_translate("MainWindow", "6"))
        self.matrixB_01.setText(_translate("MainWindow", "99"))
        self.matrixB_05.setText(_translate("MainWindow", "-7"))
        self.matrixB_02.setText(_translate("MainWindow", "104"))
        self.pushButtonPlus.setText(_translate("MainWindow", "+"))
        self.pushButtonMinus.setText(_translate("MainWindow", "-"))
        self.pushButtonMultiply.setText(_translate("MainWindow", "x"))
        self.pushButtonEqual.setText(_translate("MainWindow", "="))
        self.pushButtonDetA.setText(_translate("MainWindow", "det"))
        self.textLabel.setText(_translate("MainWindow", "welcome to matrix calculator"))
        self.pushButtonTransposeA.setText(_translate("MainWindow", "transpose"))
        self.pushButtonDetB.setText(_translate("MainWindow", "det"))
        self.pushButtonTransposeB.setText(_translate("MainWindow", "transpose"))
        self.pushButtonDetC.setText(_translate("MainWindow", "det"))
        self.pushButtonTransposeC.setText(_translate("MainWindow", "transpose"))
        self.pushButtonClearA.setText(_translate("MainWindow", "clear"))
        self.pushButtonClearB.setText(_translate("MainWindow", "clear"))
        self.pushButtonClearB_2.setText(_translate("MainWindow", "clear"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
