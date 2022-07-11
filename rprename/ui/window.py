# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(734, 704)
        self.label = QtWidgets.QLabel(Window)
        self.label.setGeometry(QtCore.QRect(10, 10, 901, 16))
        self.label.setMinimumSize(QtCore.QSize(0, 15))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Window)
        self.label_4.setGeometry(QtCore.QRect(10, 600, 711, 20))
        self.label_4.setMinimumSize(QtCore.QSize(0, 15))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(Window)
        self.progressBar.setGeometry(QtCore.QRect(10, 670, 711, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.splitter = QtWidgets.QSplitter(Window)
        self.splitter.setGeometry(QtCore.QRect(10, 110, 711, 431))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.srcFileList = QtWidgets.QListWidget(self.widget)
        self.srcFileList.setObjectName("srcFileList")
        self.verticalLayout.addWidget(self.srcFileList)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.dstFileList = QtWidgets.QListWidget(self.widget1)
        self.dstFileList.setObjectName("dstFileList")
        self.verticalLayout_2.addWidget(self.dstFileList)
        self.widget2 = QtWidgets.QWidget(Window)
        self.widget2.setGeometry(QtCore.QRect(10, 620, 711, 33))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prefixEdit = QtWidgets.QLineEdit(self.widget2)
        self.prefixEdit.setMinimumSize(QtCore.QSize(0, 15))
        self.prefixEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.prefixEdit.setObjectName("prefixEdit")
        self.horizontalLayout_2.addWidget(self.prefixEdit)
        self.extensionLabel = QtWidgets.QLabel(self.widget2)
        self.extensionLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.extensionLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.extensionLabel.setObjectName("extensionLabel")
        self.horizontalLayout_2.addWidget(self.extensionLabel)
        self.renameFilesButton = QtWidgets.QPushButton(self.widget2)
        self.renameFilesButton.setMinimumSize(QtCore.QSize(0, 15))
        self.renameFilesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.renameFilesButton.setObjectName("renameFilesButton")
        self.horizontalLayout_2.addWidget(self.renameFilesButton)
        self.widget3 = QtWidgets.QWidget(Window)
        self.widget3.setGeometry(QtCore.QRect(10, 40, 711, 33))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dirEdit = QtWidgets.QLineEdit(self.widget3)
        self.dirEdit.setMinimumSize(QtCore.QSize(0, 15))
        self.dirEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.dirEdit.setReadOnly(True)
        self.dirEdit.setObjectName("dirEdit")
        self.horizontalLayout.addWidget(self.dirEdit)
        self.loadFilesButton = QtWidgets.QPushButton(self.widget3)
        self.loadFilesButton.setMinimumSize(QtCore.QSize(0, 15))
        self.loadFilesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.loadFilesButton.setObjectName("loadFilesButton")
        self.horizontalLayout.addWidget(self.loadFilesButton)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "RP Renamer"))
        self.label.setText(_translate("Window", "Last Source Directory:"))
        self.label_4.setText(_translate("Window", "Filename Prefix:"))
        self.label_2.setText(_translate("Window", "Files To Rename"))
        self.label_3.setText(_translate("Window", "Renamed Files"))
        self.prefixEdit.setPlaceholderText(_translate("Window", "Rename your files to..."))
        self.extensionLabel.setText(_translate("Window", ".jpg"))
        self.renameFilesButton.setText(_translate("Window", "&Rename"))
        self.loadFilesButton.setText(_translate("Window", "&Load Files"))
