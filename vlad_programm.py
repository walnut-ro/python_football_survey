import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap

st1 = "What is your strongest quality?"
st2 = 'Which leg do you use better?'
st3 = 'How often do you go out \n on the field?'
st4 = 'How well do you play with your head?'
st5 = 'What would you like to win?'
st6 = 'What is your favourite possetion?'
st7 = 'What is more important for you?'
q1 = {}
q3 = {}
q4 = {}
q2 = {'Lionel Messi': 0,
      'Cristiano Ronaldo': 0,
      'Mbappe': 0,
      'Alvarez': 0,
      'Salah': 0,
      'De Bruyne': 0,
      'Rodry': 0,
      'Valverde': 0,
      'Pedry': 0,
      'Eriksen': 0,
      'van Dijk': 0,
      'Marquinhos': 0,
      'Alexander-Arnold': 0,
      'Hernandez': 0,
      'Alaba': 0,
      'Neuer': 0,
      'Alisson': 0,
      'ter Stegen': 0}
w1 = []
w2 = []
w3 = []
w4 = []
kol = 0
m1 = ''
m2 = ''
con = sqlite3.connect("Quize1_bd.sqlite")
cur = con.cursor()
idd = 1
result = cur.execute("""SELECT qualities FROM players""").fetchall()
for i in result:
    for z in i:
        w2.append(z)
result = cur.execute("""SELECT biography FROM players""").fetchall()
for i in result:
    for z in i:
        w3.append(z)
result = cur.execute("""SELECT photo FROM players""").fetchall()
for i in result:
    for z in i:
        w4.append(z)
con.close()
kol = 0
for i in q2:
    q1[i] = w2[kol]
    kol += 1
kol = 0
for i in q2:
    q3[i] = w3[kol]
    kol += 1
kol = 0
for i in q2:
    q4[i] = w4[kol]
    kol += 1
kol = 0


class Ui_Window_back1(object):
    global st1, st2, st3, st4, st5, st6, st7
    global w1, q4, m1, m2, kol

    def __init__(self):
        self.label_4 = None
        self.label_3 = None
        self.label_2 = None
        self.label_1 = None
        self.label = None
        self.label_0 = None
        self.pushButton = None
        self.centralwidget = None

    def setupUi(self, Window_back1):
        Window_back1.setObjectName("Window_back1")
        Window_back1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Window_back1.setMouseTracking(True)
        Window_back1.setTabletTracking(True)
        Window_back1.setAutoFillBackground(False)
        Window_back1.setStyleSheet("background-color: white")
        Window_back1.showMaximized()

        self.centralwidget = QtWidgets.QWidget(Window_back1)
        self.centralwidget.setObjectName("centralwidget")

        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(550, 10, 2500, 165))
        self.label_0.setObjectName("label_0")
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setItalic(True)
        font.setPointSize(24)
        self.label_0.setFont(font)
        self.label_0.setStyleSheet("")
        self.label_0.setTextFormat(QtCore.Qt.AutoText)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 320, 660, 55))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 680, 660, 55))
        self.label_1.setObjectName("label_1")
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("")
        self.label_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 990, 660, 100))
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(800, 320, 800, 55))
        self.label_3.setObjectName("label_3")
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(800, 680, 660, 55))
        self.label_4.setObjectName("label_4")
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(800, 1000, 750, 55))
        self.label_5.setObjectName("label_5")
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1700, 320, 750, 55))
        self.label_6.setObjectName("label_6")
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_result1 = QtWidgets.QLabel(self.centralwidget)
        self.label_result1.setGeometry(QtCore.QRect(1700, 700, 750, 200))
        self.label_result1.setObjectName("label_result1")
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_result1.setFont(font)
        self.label_result1.setStyleSheet("")
        self.label_result1.setTextFormat(QtCore.Qt.AutoText)
        self.label_result2 = QtWidgets.QLabel(self.centralwidget)
        self.label_result2.setGeometry(QtCore.QRect(1700, 600, 650, 150))
        self.label_result2.setObjectName("label_result2")
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_result2.setFont(font)
        self.label_result2.setStyleSheet("")
        self.label_result2.setTextFormat(QtCore.Qt.AutoText)
        self.label_result3 = QtWidgets.QLabel(self.centralwidget)
        self.label_result3.setGeometry(QtCore.QRect(1700, 900, 800, 850))
        self.label_result3.setObjectName("label_result3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1000, 220, 250, 50))
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setFamily("Niagara Solid")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(30)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("border-radius: 0px")
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)

        self.buttonGroup = QtWidgets.QButtonGroup(Window_back1)
        self.buttonGroup.setObjectName("buttonGroup")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QtCore.QRect(50, 400, 200, 40))
        self.radioButton.setObjectName("radioButton")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setFont(font)
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 450, 200, 40))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setFont(font)
        self.radioButton_2.setFont(font)
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 500, 200, 40))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setFont(font)
        self.radioButton_3.setFont(font)
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setEnabled(False)
        self.radioButton_4.setGeometry(QtCore.QRect(50, 550, 200, 40))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.setFont(font)
        self.radioButton_4.setFont(font)
        self.buttonGroup.addButton(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setEnabled(False)
        self.radioButton_5.setGeometry(QtCore.QRect(50, 600, 200, 40))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_5.setFont(font)
        self.radioButton_5.setFont(font)
        self.buttonGroup.addButton(self.radioButton_5)

        self.buttonGroup_2 = QtWidgets.QButtonGroup(Window_back1)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setEnabled(False)
        self.radioButton_6.setGeometry(QtCore.QRect(50, 760, 250, 40))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_6.setFont(font)
        self.radioButton_6.setFont(font)
        self.buttonGroup_2.addButton(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setEnabled(False)
        self.radioButton_7.setGeometry(QtCore.QRect(50, 810, 250, 40))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_7.setFont(font)
        self.radioButton_7.setFont(font)
        self.buttonGroup_2.addButton(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setEnabled(False)
        self.radioButton_8.setGeometry(QtCore.QRect(50, 860, 250, 40))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_8.setFont(font)
        self.radioButton_8.setFont(font)
        self.buttonGroup_2.addButton(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9.setEnabled(False)
        self.radioButton_9.setGeometry(QtCore.QRect(50, 910, 250, 40))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_9.setFont(font)
        self.radioButton_9.setFont(font)
        self.buttonGroup_2.addButton(self.radioButton_9)

        self.buttonGroup_3 = QtWidgets.QButtonGroup(Window_back1)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setEnabled(False)
        self.radioButton_10.setGeometry(QtCore.QRect(50, 1115, 250, 40))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_10.setFont(font)
        self.radioButton_10.setFont(font)
        self.buttonGroup_3.addButton(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_11.setEnabled(False)
        self.radioButton_11.setGeometry(QtCore.QRect(50, 1165, 250, 40))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_11.setFont(font)
        self.radioButton_11.setFont(font)
        self.buttonGroup_3.addButton(self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_12.setEnabled(False)
        self.radioButton_12.setGeometry(QtCore.QRect(50, 1215, 250, 40))
        self.radioButton_12.setObjectName("radioButton_12")
        self.radioButton_12.setFont(font)
        self.radioButton_12.setFont(font)
        self.buttonGroup_3.addButton(self.radioButton_12)
        self.radioButton_13 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_13.setEnabled(False)
        self.radioButton_13.setGeometry(QtCore.QRect(50, 1265, 250, 40))
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_13.setFont(font)
        self.radioButton_13.setFont(font)
        self.buttonGroup_3.addButton(self.radioButton_13)

        self.buttonGroup_4 = QtWidgets.QButtonGroup(Window_back1)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.radioButton_14 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_14.setEnabled(False)
        self.radioButton_14.setGeometry(QtCore.QRect(820, 400, 500, 40))
        self.radioButton_14.setObjectName("radioButton_14")
        self.radioButton_14.setFont(font)
        self.radioButton_14.setFont(font)
        self.buttonGroup_4.addButton(self.radioButton_14)
        self.radioButton_15 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_15.setEnabled(False)
        self.radioButton_15.setGeometry(QtCore.QRect(820, 450, 500, 40))
        self.radioButton_15.setObjectName("radioButton_15")
        self.radioButton_15.setFont(font)
        self.radioButton_15.setFont(font)
        self.buttonGroup_4.addButton(self.radioButton_15)
        self.radioButton_16 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_16.setEnabled(False)
        self.radioButton_16.setGeometry(QtCore.QRect(820, 500, 500, 40))
        self.radioButton_16.setObjectName("radioButton_16")
        self.radioButton_16.setFont(font)
        self.radioButton_16.setFont(font)
        self.buttonGroup_4.addButton(self.radioButton_16)
        self.radioButton_17 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_17.setEnabled(False)
        self.radioButton_17.setGeometry(QtCore.QRect(820, 550, 500, 40))
        self.radioButton_17.setObjectName("radioButton_17")
        self.radioButton_17.setFont(font)
        self.radioButton_17.setFont(font)
        self.buttonGroup_4.addButton(self.radioButton_17)

        self.buttonGroup_5 = QtWidgets.QButtonGroup(Window_back1)
        self.buttonGroup_5.setObjectName("buttonGroup_5")
        self.radioButton_18 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_18.setEnabled(False)
        self.radioButton_18.setGeometry(QtCore.QRect(820, 760, 310, 40))
        self.radioButton_18.setObjectName("radioButton_18")
        self.radioButton_18.setFont(font)
        self.radioButton_18.setFont(font)
        self.buttonGroup_5.addButton(self.radioButton_18)
        self.radioButton_19 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_19.setEnabled(False)
        self.radioButton_19.setGeometry(QtCore.QRect(820, 810, 310, 40))
        self.radioButton_19.setObjectName("radioButton_19")
        self.radioButton_19.setFont(font)
        self.radioButton_19.setFont(font)
        self.buttonGroup_5.addButton(self.radioButton_19)
        self.radioButton_20 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_20.setEnabled(False)
        self.radioButton_20.setGeometry(QtCore.QRect(820, 860, 310, 40))
        self.radioButton_20.setObjectName("radioButton_20")
        self.radioButton_20.setFont(font)
        self.radioButton_20.setFont(font)
        self.buttonGroup_5.addButton(self.radioButton_20)
        self.radioButton_21 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_21.setEnabled(False)
        self.radioButton_21.setGeometry(QtCore.QRect(820, 910, 310, 40))
        self.radioButton_21.setObjectName("radioButton_21")
        self.radioButton_21.setFont(font)
        self.radioButton_21.setFont(font)
        self.buttonGroup_5.addButton(self.radioButton_21)

        self.buttonGroup_6 = QtWidgets.QButtonGroup(Window_back1)
        self.buttonGroup_6.setObjectName("buttonGroup_6")
        self.radioButton_22 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_22.setEnabled(False)
        self.radioButton_22.setGeometry(QtCore.QRect(820, 1115, 250, 40))
        self.radioButton_22.setObjectName("radioButton_22")
        self.radioButton_22.setFont(font)
        self.radioButton_22.setFont(font)
        self.buttonGroup_6.addButton(self.radioButton_22)
        self.radioButton_23 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_23.setEnabled(False)
        self.radioButton_23.setGeometry(QtCore.QRect(820, 1165, 250, 40))
        self.radioButton_23.setObjectName("radioButton_23")
        self.radioButton_23.setFont(font)
        self.radioButton_23.setFont(font)
        self.buttonGroup_6.addButton(self.radioButton_23)
        self.radioButton_24 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_24.setEnabled(False)
        self.radioButton_24.setGeometry(QtCore.QRect(820, 1215, 250, 40))
        self.radioButton_24.setObjectName("radioButton_24")
        self.radioButton_24.setFont(font)
        self.radioButton_24.setFont(font)
        self.buttonGroup_6.addButton(self.radioButton_24)
        self.radioButton_25 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_25.setEnabled(False)
        self.radioButton_25.setGeometry(QtCore.QRect(820, 1265, 250, 40))
        self.radioButton_25.setObjectName("radioButton_25")
        self.radioButton_25.setFont(font)
        self.radioButton_25.setFont(font)
        self.buttonGroup_6.addButton(self.radioButton_25)

        self.buttonGroup_7 = QtWidgets.QButtonGroup(Window_back1)
        self.buttonGroup_7.setObjectName("buttonGroup_7")
        self.radioButton_26 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_26.setEnabled(False)
        self.radioButton_26.setGeometry(QtCore.QRect(1720, 400, 510, 35))
        self.radioButton_26.setObjectName("radioButton_26")
        self.radioButton_26.setFont(font)
        self.radioButton_26.setFont(font)
        self.buttonGroup_7.addButton(self.radioButton_26)
        self.radioButton_27 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_27.setEnabled(False)
        self.radioButton_27.setGeometry(QtCore.QRect(1720, 450, 510, 35))
        self.radioButton_27.setObjectName("radioButton_27")
        self.radioButton_27.setFont(font)
        self.radioButton_27.setFont(font)
        self.buttonGroup_7.addButton(self.radioButton_27)
        self.radioButton_28 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_28.setEnabled(False)
        self.radioButton_28.setGeometry(QtCore.QRect(1720, 500, 510, 35))
        self.radioButton_28.setObjectName("radioButton_28")
        self.radioButton_28.setFont(font)
        self.radioButton_28.setFont(font)
        self.buttonGroup_7.addButton(self.radioButton_28)
        self.radioButton_29 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_29.setEnabled(False)
        self.radioButton_29.setGeometry(QtCore.QRect(1720, 550, 510, 35))
        self.radioButton_29.setObjectName("radioButton_29")
        self.radioButton_29.setFont(font)
        self.radioButton_29.setFont(font)
        self.buttonGroup_7.addButton(self.radioButton_29)

        Window_back1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window_back1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Window_back1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window_back1)
        self.statusbar.setObjectName("statusbar")
        Window_back1.setStatusBar(self.statusbar)

        self.retranslateUi(Window_back1)
        self.pushButton.clicked.connect(self.first_question)
        QtCore.QMetaObject.connectSlotsByName(Window_back1)

        self.w = QWidget()
        self.layout = QVBoxLayout()
        self.w.setLayout(self.layout)
        self.pixmap = QPixmap()

    def retranslateUi(self, Window_back1):
        _translate = QtCore.QCoreApplication.translate
        Window_back1.setWindowTitle(_translate("Window_back1", "Guess who you are"))
        self.label_0.setText(_translate("Window_back", "                           If You opened this app, \n"
                                                       "then you want to find out who you are from football players!"))
        self.label.setText(_translate("Window_back1", st1))
        self.label_1.setText(_translate("Window_back1", st2))
        self.label_2.setText(_translate("Window_back1", st3))
        self.label_3.setText(_translate("Window_back1", st4))
        self.label_4.setText(_translate("Window_back1", st5))
        self.label_5.setText(_translate("Window_back1", st6))
        self.label_6.setText(_translate("Window_back1", st7))

        self.pushButton.setText(_translate("Window_back", "Let\'s Start!"))

        self.radioButton.setText(_translate("Window_back1", "speed"))
        self.radioButton_2.setText(_translate("Window_back1", "shooting"))
        self.radioButton_3.setText(_translate("Window_back1", "passing"))
        self.radioButton_4.setText(_translate("Window_back1", "dribbling"))
        self.radioButton_5.setText(_translate("Window_back1", "defending"))
        self.radioButton_6.setText(_translate("Window_back1", "left"))
        self.radioButton_7.setText(_translate("Window_back1", "right"))
        self.radioButton_8.setText(_translate("Window_back1", "both"))
        self.radioButton_9.setText(_translate("Window_back1", "I don't know"))
        self.radioButton_10.setText(_translate("Window_back1", "always"))
        self.radioButton_11.setText(_translate("Window_back1", "regularly"))
        self.radioButton_12.setText(_translate("Window_back1", "infrequently"))
        self.radioButton_13.setText(_translate("Window_back1", "never"))
        self.radioButton_14.setText(_translate("Window_back1", "very well"))
        self.radioButton_15.setText(_translate("Window_back1", "I can't play"))
        self.radioButton_16.setText(_translate("Window_back1", "I try not to play"))
        self.radioButton_17.setText(_translate("Window_back1", "depending on the degree"))
        self.radioButton_18.setText(_translate("Window_back1", "Champions League"))
        self.radioButton_19.setText(_translate("Window_back1", "World Cup"))
        self.radioButton_20.setText(_translate("Window_back1", "own League"))
        self.radioButton_21.setText(_translate("Window_back1", "it doesn't matter"))
        self.radioButton_22.setText(_translate("Window_back1", "striker"))
        self.radioButton_23.setText(_translate("Window_back1", "midfielder"))
        self.radioButton_24.setText(_translate("Window_back1", "defender"))
        self.radioButton_25.setText(_translate("Window_back1", "goalkeeper"))
        self.radioButton_26.setText(_translate("Window_back1", "score the goal"))
        self.radioButton_27.setText(_translate("Window_back1", "do the assist"))
        self.radioButton_28.setText(_translate("Window_back1", "don't miss a goal"))
        self.radioButton_29.setText(_translate("Window_back1", "the most important is the victory"))

    def first_question(self):
        self.radioButton.setEnabled(True)
        self.radioButton_2.setEnabled(True)
        self.radioButton_3.setEnabled(True)
        self.radioButton_4.setEnabled(True)
        self.radioButton_5.setEnabled(True)
        self.radioButton.clicked.connect(self.second_question)
        self.radioButton_2.clicked.connect(self.second_question)
        self.radioButton_3.clicked.connect(self.second_question)
        self.radioButton_4.clicked.connect(self.second_question)
        self.radioButton_5.clicked.connect(self.second_question)

    def second_question(self):
        w1.append(self.buttonGroup.checkedButton().text())
        self.radioButton_6.setEnabled(True)
        self.radioButton_7.setEnabled(True)
        self.radioButton_8.setEnabled(True)
        self.radioButton_9.setEnabled(True)
        self.radioButton.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.radioButton_3.setEnabled(False)
        self.radioButton_4.setEnabled(False)
        self.radioButton_5.setEnabled(False)
        self.radioButton_6.clicked.connect(self.third_question)
        self.radioButton_7.clicked.connect(self.third_question)
        self.radioButton_8.clicked.connect(self.third_question)
        self.radioButton_9.clicked.connect(self.third_question)

    def third_question(self):
        w1.append(self.buttonGroup_2.checkedButton().text())
        self.radioButton_10.setEnabled(True)
        self.radioButton_11.setEnabled(True)
        self.radioButton_12.setEnabled(True)
        self.radioButton_13.setEnabled(True)
        self.radioButton_6.setEnabled(False)
        self.radioButton_7.setEnabled(False)
        self.radioButton_8.setEnabled(False)
        self.radioButton_9.setEnabled(False)
        self.radioButton_10.clicked.connect(self.fourth_question)
        self.radioButton_11.clicked.connect(self.fourth_question)
        self.radioButton_12.clicked.connect(self.fourth_question)
        self.radioButton_13.clicked.connect(self.fourth_question)

    def fourth_question(self):
        w1.append(self.buttonGroup_3.checkedButton().text())
        self.radioButton_14.setEnabled(True)
        self.radioButton_15.setEnabled(True)
        self.radioButton_16.setEnabled(True)
        self.radioButton_17.setEnabled(True)
        self.radioButton_10.setEnabled(False)
        self.radioButton_11.setEnabled(False)
        self.radioButton_12.setEnabled(False)
        self.radioButton_13.setEnabled(False)
        self.radioButton_14.clicked.connect(self.fifth_question)
        self.radioButton_15.clicked.connect(self.fifth_question)
        self.radioButton_16.clicked.connect(self.fifth_question)
        self.radioButton_17.clicked.connect(self.fifth_question)

    def fifth_question(self):
        w1.append(self.buttonGroup_4.checkedButton().text())
        self.radioButton_18.setEnabled(True)
        self.radioButton_19.setEnabled(True)
        self.radioButton_20.setEnabled(True)
        self.radioButton_21.setEnabled(True)
        self.radioButton_14.setEnabled(False)
        self.radioButton_15.setEnabled(False)
        self.radioButton_16.setEnabled(False)
        self.radioButton_17.setEnabled(False)
        self.radioButton_18.clicked.connect(self.sixth_question)
        self.radioButton_19.clicked.connect(self.sixth_question)
        self.radioButton_20.clicked.connect(self.sixth_question)
        self.radioButton_21.clicked.connect(self.sixth_question)

    def sixth_question(self):
        w1.append(self.buttonGroup_5.checkedButton().text())
        self.radioButton_22.setEnabled(True)
        self.radioButton_23.setEnabled(True)
        self.radioButton_24.setEnabled(True)
        self.radioButton_25.setEnabled(True)
        self.radioButton_18.setEnabled(False)
        self.radioButton_19.setEnabled(False)
        self.radioButton_20.setEnabled(False)
        self.radioButton_21.setEnabled(False)
        self.radioButton_22.clicked.connect(self.seventh_question)
        self.radioButton_23.clicked.connect(self.seventh_question)
        self.radioButton_24.clicked.connect(self.seventh_question)
        self.radioButton_25.clicked.connect(self.seventh_question)

    def seventh_question(self):
        w1.append(self.buttonGroup_6.checkedButton().text())
        w1.append(self.buttonGroup_6.checkedButton().text())
        self.radioButton_26.setEnabled(True)
        self.radioButton_27.setEnabled(True)
        self.radioButton_28.setEnabled(True)
        self.radioButton_29.setEnabled(True)
        self.radioButton_22.setEnabled(False)
        self.radioButton_23.setEnabled(False)
        self.radioButton_24.setEnabled(False)
        self.radioButton_25.setEnabled(False)
        self.radioButton_26.clicked.connect(self.results)
        self.radioButton_27.clicked.connect(self.results)
        self.radioButton_28.clicked.connect(self.results)
        self.radioButton_29.clicked.connect(self.results)

    def results(self):
        w1.append(self.buttonGroup_7.checkedButton().text())
        self.radioButton_26.setEnabled(False)
        self.radioButton_27.setEnabled(False)
        self.radioButton_28.setEnabled(False)
        self.radioButton_29.setEnabled(False)
        for p in w1:
            for elem in q2:
                if p in q1[elem]:
                    q2[elem] += 1
        kol = q2['Lionel Messi']
        m1 = 'Lionel Messi'
        m2 = q3[m1]
        for p in q2:
            if q2[p] > kol:
                m1 = p
                m2 = q3[p]

        m3 = f"<a href=\"{m2}\"> Узнать больше <a/>"
        self.label_result1.setText(m3)
        self.label_result1.setOpenExternalLinks(True)
        self.label_result2.setText(f'I think you are: {m1}')
        for i in q4:
            if i == m1:
                self.pixmap.loadFromData(q4[m1])
                self.label_result3.setPixmap(self.pixmap)
                break


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_back1 = QtWidgets.QMainWindow()
    ui = Ui_Window_back1()
    ui.setupUi(Window_back1)
    Window_back1.show()
    sys.exit(app.exec_())