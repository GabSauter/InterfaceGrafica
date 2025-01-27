# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Programacao\Python\IGDefinitiva\UIFolder\MainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 701)
        MainWindow.setStyleSheet("#MainWindow{\n"
                                 "    background-color: #E6E6EA;\n"
                                 "}\n"
                                 "QLineEdit{\n"
                                 "    background-color: #F4F4F8;\n"
                                 "    border-radius: 8px;\n"
                                 "    border: 1px solid;\n"
                                 "   padding: 2px 2px 2px 5px;\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "   background-color: #FED766;\n"
                                 "    border-radius: 8px;\n"
                                 "   height: 20px;\n"
                                 "    border: 1px solid;\n"
                                 "}\n"
                                 "QFrame{\n"
                                 "    border: 1px solid;\n"
                                 "}\n"
                                 "QLabel{\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 211, 322))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtPonto = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.txtPonto.setAlignment(QtCore.Qt.AlignCenter)
        self.txtPonto.setObjectName("txtPonto")
        self.verticalLayout_2.addWidget(self.txtPonto)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editX = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editX.setObjectName("editX")
        self.horizontalLayout.addWidget(self.editX)
        self.editY = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editY.setObjectName("editY")
        self.horizontalLayout.addWidget(self.editY)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.btnCreatePoint = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)
        self.btnCreatePoint.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnCreatePoint.setObjectName("btnCreatePoint")
        self.verticalLayout_2.addWidget(self.btnCreatePoint)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.txtTriangle = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.txtTriangle.setAlignment(QtCore.Qt.AlignCenter)
        self.txtTriangle.setObjectName("txtTriangle")
        self.verticalLayout_2.addWidget(self.txtTriangle)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.editTriangleX_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editTriangleX_2.setObjectName("editTriangleX_2")
        self.horizontalLayout_3.addWidget(self.editTriangleX_2)
        self.editTriangleY_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editTriangleY_2.setObjectName("editTriangleY_2")
        self.horizontalLayout_3.addWidget(self.editTriangleY_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.editTriangleX_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editTriangleX_3.setObjectName("editTriangleX_3")
        self.horizontalLayout_4.addWidget(self.editTriangleX_3)
        self.editTriangleY_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editTriangleY_3.setObjectName("editTriangleY_3")
        self.horizontalLayout_4.addWidget(self.editTriangleY_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editTriangleX = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editTriangleX.setObjectName("editTriangleX")
        self.horizontalLayout_2.addWidget(self.editTriangleX)
        self.editTriangleY = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editTriangleY.setObjectName("editTriangleY")
        self.horizontalLayout_2.addWidget(self.editTriangleY)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btnCreateTriangle = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)
        self.btnCreateTriangle.setObjectName("btnCreateTriangle")
        self.verticalLayout.addWidget(self.btnCreateTriangle)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.txtPoligono = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.txtPoligono.setAlignment(QtCore.Qt.AlignCenter)
        self.txtPoligono.setObjectName("txtPoligono")
        self.verticalLayout_5.addWidget(self.txtPoligono)
        self.editPolygon = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editPolygon.setObjectName("editPolygon")
        self.verticalLayout_5.addWidget(self.editPolygon)
        self.btnCreatePolygon = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)
        self.btnCreatePolygon.setObjectName("btnCreatePolygon")
        self.verticalLayout_5.addWidget(self.btnCreatePolygon)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(
            QtCore.QRect(10, 350, 211, 295))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.txtTranslation = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txtTranslation.sizePolicy().hasHeightForWidth())
        self.txtTranslation.setSizePolicy(sizePolicy)
        self.txtTranslation.setAlignment(QtCore.Qt.AlignCenter)
        self.txtTranslation.setObjectName("txtTranslation")
        self.horizontalLayout_6.addWidget(self.txtTranslation)
        self.editTranslation = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.editTranslation.sizePolicy().hasHeightForWidth())
        self.editTranslation.setSizePolicy(sizePolicy)
        self.editTranslation.setObjectName("editTranslation")
        self.horizontalLayout_6.addWidget(self.editTranslation)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnUp = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnUp.setObjectName("btnUp")
        self.gridLayout_2.addWidget(self.btnUp, 0, 1, 1, 1)
        self.btnDown = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnDown.setObjectName("btnDown")
        self.gridLayout_2.addWidget(self.btnDown, 1, 1, 1, 1)
        self.btnLeft = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnLeft.setObjectName("btnLeft")
        self.gridLayout_2.addWidget(self.btnLeft, 1, 0, 1, 1)
        self.btnRight = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnRight.setObjectName("btnRight")
        self.gridLayout_2.addWidget(self.btnRight, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.editRotate = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.editRotate.sizePolicy().hasHeightForWidth())
        self.editRotate.setSizePolicy(sizePolicy)
        self.editRotate.setObjectName("editRotate")
        self.horizontalLayout_9.addWidget(self.editRotate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btnRotateLeft = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnRotateLeft.setObjectName("btnRotateLeft")
        self.horizontalLayout_8.addWidget(self.btnRotateLeft)
        self.btnRotateRight = QtWidgets.QPushButton(
            self.verticalLayoutWidget_3)
        self.btnRotateRight.setObjectName("btnRotateRight")
        self.horizontalLayout_8.addWidget(self.btnRotateRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.editScale = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.editScale.sizePolicy().hasHeightForWidth())
        self.editScale.setSizePolicy(sizePolicy)
        self.editScale.setObjectName("editScale")
        self.horizontalLayout_10.addWidget(self.editScale)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btnScaleMinus = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnScaleMinus.setObjectName("btnScaleMinus")
        self.horizontalLayout_11.addWidget(self.btnScaleMinus)
        self.btnScalePlus = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnScalePlus.setObjectName("btnScalePlus")
        self.horizontalLayout_11.addWidget(self.btnScalePlus)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.txtBezierCurve = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.txtBezierCurve.setAlignment(QtCore.Qt.AlignCenter)
        self.txtBezierCurve.setObjectName("txtBezierCurve")
        self.verticalLayout_4.addWidget(self.txtBezierCurve)
        self.editBezierCurve = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.editBezierCurve.setObjectName("editBezierCurve")
        self.verticalLayout_4.addWidget(self.editBezierCurve)
        self.btnCreateBezierCurve = QtWidgets.QPushButton(
            self.verticalLayoutWidget_3)
        self.btnCreateBezierCurve.setObjectName("btnCreateBezierCurve")
        self.verticalLayout_4.addWidget(self.btnCreateBezierCurve)

        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.viewPort = QtWidgets.QWidget(self.centralwidget)
        self.viewPort.setGeometry(QtCore.QRect(240, 10, 550, 550))
        self.viewPort.setObjectName("viewPort")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txtPonto.setText(_translate("MainWindow", "Ponto"))
        self.btnCreatePoint.setText(_translate("MainWindow", "Criar Ponto"))
        self.txtTriangle.setText(_translate("MainWindow", "Triângulo"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.btnCreateTriangle.setText(
            _translate("MainWindow", "Criar Triângulo"))
        self.txtPoligono.setText(_translate("MainWindow", "Polígono"))
        self.editPolygon.setPlaceholderText(
            _translate("MainWindow", "x1,y1,x2,y2..."))
        self.btnCreatePolygon.setText(
            _translate("MainWindow", "Criar Polígono"))
        self.txtTranslation.setText(_translate("MainWindow", "Translação"))
        self.btnUp.setText(_translate("MainWindow", "^"))
        self.btnDown.setText(_translate("MainWindow", "v"))
        self.btnLeft.setText(_translate("MainWindow", "<"))
        self.btnRight.setText(_translate("MainWindow", ">"))
        self.label_3.setText(_translate("MainWindow", "Rotação"))
        self.btnRotateLeft.setText(_translate("MainWindow", "<-"))
        self.btnRotateRight.setText(_translate("MainWindow", "->"))
        self.label_4.setText(_translate("MainWindow", "Escala"))
        self.btnScaleMinus.setText(_translate("MainWindow", "-"))
        self.btnScalePlus.setText(_translate("MainWindow", "+"))
        self.txtBezierCurve.setText(_translate(
            "MainWindow", "Curva de Bézier - x1,y1,x2,y2..."))
        self.btnCreateBezierCurve.setText(
            _translate("MainWindow", "Criar curva de Bézier"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
