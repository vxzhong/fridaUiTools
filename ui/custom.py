# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'custom.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CustomDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(951, 706)
        self.gridLayout_5 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.tabCustomList = QtWidgets.QTableWidget(self.groupBox)
        self.tabCustomList.setObjectName("tabCustomList")
        self.tabCustomList.setColumnCount(0)
        self.tabCustomList.setRowCount(0)
        self.gridLayout.addWidget(self.tabCustomList, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabCustomHookList = QtWidgets.QTableWidget(self.groupBox_3)
        self.tabCustomHookList.setObjectName("tabCustomHookList")
        self.tabCustomHookList.setColumnCount(0)
        self.tabCustomHookList.setRowCount(0)
        self.gridLayout_2.addWidget(self.tabCustomHookList, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.txtJsName = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtJsName.setObjectName("txtJsName")
        self.gridLayout_3.addWidget(self.txtJsName, 0, 1, 1, 1)
        self.btnSubmit = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSubmit.setObjectName("btnSubmit")
        self.gridLayout_3.addWidget(self.btnSubmit, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtJsData = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.txtJsData.setObjectName("txtJsData")
        self.gridLayout_3.addWidget(self.txtJsData, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_4, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "自定义"))
        self.groupBox.setTitle(_translate("Dialog", "自定义脚本列表"))
        self.groupBox_3.setTitle(_translate("Dialog", "使用脚本列表"))
        self.groupBox_2.setTitle(_translate("Dialog", "添加自定义脚本"))
        self.label.setText(_translate("Dialog", "脚本别名："))
        self.btnSubmit.setText(_translate("Dialog", "添加"))
        self.label_2.setText(_translate("Dialog", "HOOK脚本："))
        self.groupBox_4.setTitle(_translate("Dialog", "操作提示"))
        self.label_3.setText(_translate("Dialog", "双击自定义脚本列表的项目添加到使用列表，窗口关闭会添加使用列表的项到hook的列表"))
        self.label_4.setText(_translate("Dialog", "保存的脚本存放在custom目录，自定义脚本列表右键删除会删掉对应的文件"))

