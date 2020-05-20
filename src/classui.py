# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../asset/tpl/classui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_classForm(object):
    def setupUi(self, classForm):
        classForm.setObjectName("classForm")
        classForm.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/asset/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        classForm.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(classForm)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(classForm)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.classLabel = QtWidgets.QLabel(classForm)
        self.classLabel.setObjectName("classLabel")
        self.gridLayout.addWidget(self.classLabel, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(295, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.classTextEdit = QtWidgets.QTextEdit(classForm)
        self.classTextEdit.setObjectName("classTextEdit")
        self.gridLayout.addWidget(self.classTextEdit, 1, 0, 1, 3)

        self.retranslateUi(classForm)
        QtCore.QMetaObject.connectSlotsByName(classForm)

    def retranslateUi(self, classForm):
        _translate = QtCore.QCoreApplication.translate
        classForm.setWindowTitle(_translate("classForm", "Form"))
        self.label.setText(_translate("classForm", "类名："))
        self.classLabel.setText(_translate("classForm", "class0"))
import img_rc
