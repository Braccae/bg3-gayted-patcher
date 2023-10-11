# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 595)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 469, 801, 101))
        self.consoleLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.consoleLayout.setObjectName(u"consoleLayout")
        self.consoleLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.horizontalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 797, 97))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.consoleLayout.addWidget(self.scrollArea)

        self.verticalTabWidget = QTabWidget(self.centralwidget)
        self.verticalTabWidget.setObjectName(u"verticalTabWidget")
        self.verticalTabWidget.setGeometry(QRect(0, 0, 801, 451))
        self.tab_modExtraction = QWidget()
        self.tab_modExtraction.setObjectName(u"tab_modExtraction")
        self.horizontalLayoutWidget_2 = QWidget(self.tab_modExtraction)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 10, 801, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_4)

        self.textfield_modDir = QLineEdit(self.horizontalLayoutWidget_2)
        self.textfield_modDir.setObjectName(u"textfield_modDir")

        self.horizontalLayout_2.addWidget(self.textfield_modDir)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_3)

        self.checkbox_autodetectMods = QCheckBox(self.horizontalLayoutWidget_2)
        self.checkbox_autodetectMods.setObjectName(u"checkbox_autodetectMods")

        self.horizontalLayout_2.addWidget(self.checkbox_autodetectMods)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_2)

        self.button_extractProgressions = QPushButton(self.horizontalLayoutWidget_2)
        self.button_extractProgressions.setObjectName(u"button_extractProgressions")

        self.horizontalLayout_2.addWidget(self.button_extractProgressions)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer)

        self.verticalTabWidget.addTab(self.tab_modExtraction, "")
        self.tab_mergeProgressions = QWidget()
        self.tab_mergeProgressions.setObjectName(u"tab_mergeProgressions")
        self.verticalTabWidget.addTab(self.tab_mergeProgressions, "")
        self.tab_modifyProgressions = QWidget()
        self.tab_modifyProgressions.setObjectName(u"tab_modifyProgressions")
        self.verticalTabWidget.addTab(self.tab_modifyProgressions, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.verticalTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkbox_autodetectMods.setText(QCoreApplication.translate("MainWindow", u"use autodetected user directories", None))
        self.button_extractProgressions.setText(QCoreApplication.translate("MainWindow", u"Extract Progressions.lsx", None))
        self.verticalTabWidget.setTabText(self.verticalTabWidget.indexOf(self.tab_modExtraction), QCoreApplication.translate("MainWindow", u"Extract Progressions", None))
        self.verticalTabWidget.setTabText(self.verticalTabWidget.indexOf(self.tab_mergeProgressions), QCoreApplication.translate("MainWindow", u"Merge", None))
        self.verticalTabWidget.setTabText(self.verticalTabWidget.indexOf(self.tab_modifyProgressions), QCoreApplication.translate("MainWindow", u"Modify", None))
    # retranslateUi

