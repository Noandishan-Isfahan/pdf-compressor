from setting import ROOT_DIR
from pathlib import Path
from src.ui.custom.Widget import CustomLabel,CustomPushButton
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(750, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QSize(750, 350))
        mainWindow.setMaximumSize(QSize(750, 350))
        font = QFont()
        font.setFamilies([u"Vazirmatn"])
        mainWindow.setFont(font)
        self.menu_openfile = QAction(mainWindow)
        self.menu_openfile.setObjectName(u"menu_openfile")
        self.menu_openfile.setFont(font)
        self.menu_savefile = QAction(mainWindow)
        self.menu_savefile.setObjectName(u"menu_savefile")
        self.menu_savefile.setFont(font)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(750, 325))
        self.centralwidget.setMaximumSize(QSize(750, 325))
        self.centralwidget.setFont(font)
        self.centralwidget.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 80))
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = CustomLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Vazirmatn"])
        font1.setPointSize(19)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label)

        self.lbl_logo = CustomLabel(self.groupBox)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setMinimumSize(QSize(60, 60))
        self.lbl_logo.setMaximumSize(QSize(60, 60))
        self.lbl_logo.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.lbl_logo)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 250))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupBox_2.setFlat(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(300, 250))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupBox_3.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(270, 60))
        self.groupBox_5.setMaximumSize(QSize(300, 60))
        self.groupBox_5.setFont(font)
        self.groupBox_5.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_2 = CustomLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(115, 0))
        font2 = QFont()
        font2.setFamilies([u"Vazirmatn"])
        font2.setPointSize(11)
        self.label_2.setFont(font2)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.label_2)

        self.txt_color_image_res = QLineEdit(self.groupBox_5)
        self.txt_color_image_res.setObjectName(u"txt_color_image_res")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txt_color_image_res.sizePolicy().hasHeightForWidth())
        self.txt_color_image_res.setSizePolicy(sizePolicy1)
        self.txt_color_image_res.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.txt_color_image_res)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(270, 60))
        self.groupBox_6.setMaximumSize(QSize(300, 60))
        self.groupBox_6.setFont(font)
        self.groupBox_6.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_3 = CustomLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(115, 0))
        self.label_3.setFont(font2)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.txt_gray_image_res = QLineEdit(self.groupBox_6)
        self.txt_gray_image_res.setObjectName(u"txt_gray_image_res")
        sizePolicy1.setHeightForWidth(self.txt_gray_image_res.sizePolicy().hasHeightForWidth())
        self.txt_gray_image_res.setSizePolicy(sizePolicy1)
        self.txt_gray_image_res.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.txt_gray_image_res)


        self.verticalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(270, 60))
        self.groupBox_7.setMaximumSize(QSize(300, 60))
        self.groupBox_7.setFont(font)
        self.groupBox_7.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_4 = CustomLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(115, 0))
        self.label_4.setFont(font2)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.txt_mono_image_res = QLineEdit(self.groupBox_7)
        self.txt_mono_image_res.setObjectName(u"txt_mono_image_res")
        sizePolicy1.setHeightForWidth(self.txt_mono_image_res.sizePolicy().hasHeightForWidth())
        self.txt_mono_image_res.setSizePolicy(sizePolicy1)
        self.txt_mono_image_res.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_4.addWidget(self.txt_mono_image_res)


        self.verticalLayout_2.addWidget(self.groupBox_7)


        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(500, 250))
        self.groupBox_4.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_9 = QGroupBox(self.groupBox_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_openfile = CustomPushButton(self.groupBox_9)
        self.btn_openfile.setObjectName(u"btn_openfile")

        self.verticalLayout_3.addWidget(self.btn_openfile)

        self.btn_convert = CustomPushButton(self.groupBox_9)
        self.btn_convert.setObjectName(u"btn_convert")

        self.verticalLayout_3.addWidget(self.btn_convert)

        self.btn_savefile = CustomPushButton(self.groupBox_9)
        self.btn_savefile.setObjectName(u"btn_savefile")

        self.verticalLayout_3.addWidget(self.btn_savefile)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.groupBox_9)

        self.groupBox_8 = QGroupBox(self.groupBox_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout = QVBoxLayout(self.groupBox_8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_12 = QGroupBox(self.groupBox_8)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(0, 40))
        self.groupBox_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = CustomLabel(self.groupBox_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.lbl_file_size = CustomLabel(self.groupBox_12)
        self.lbl_file_size.setObjectName(u"lbl_file_size")
        self.lbl_file_size.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.lbl_file_size)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout.addWidget(self.groupBox_12)

        self.groupBox_11 = QGroupBox(self.groupBox_8)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(0, 40))
        self.groupBox_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = CustomLabel(self.groupBox_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lbl_file_name = CustomLabel(self.groupBox_11)
        self.lbl_file_name.setObjectName(u"lbl_file_name")
        self.lbl_file_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lbl_file_name)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)

        self.verticalLayout.addWidget(self.groupBox_11)

        self.groupBox_10 = QGroupBox(self.groupBox_8)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(0, 40))
        self.groupBox_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = CustomLabel(self.groupBox_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lbl_file_after_size = CustomLabel(self.groupBox_10)
        self.lbl_file_after_size.setObjectName(u"lbl_file_after_size")
        self.lbl_file_after_size.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lbl_file_after_size)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout.addWidget(self.groupBox_10)

        self.verticalSpacer_3 = QSpacerItem(20, 26, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.groupBox_8)


        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 750, 24))
        self.menubar.setFont(font)
        self.menubar.setLayoutDirection(Qt.RightToLeft)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setFont(font)
        mainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.menu_openfile)
        self.menu.addAction(self.menu_savefile)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u0641\u0634\u0631\u062f\u0647 \u0633\u0627\u0632\u06cc", None))
        self.menu_openfile.setText(QCoreApplication.translate("mainWindow", u"\u0628\u0627\u0632\u06a9\u0631\u062f\u0646 \u0641\u0627\u06cc\u0644", None))
        self.menu_savefile.setText(QCoreApplication.translate("mainWindow", u"\u0630\u062e\u06cc\u0631\u0647", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u0646\u0631\u0645\u200c\u0627\u0641\u0632\u0627\u0631 \u0641\u0634\u0631\u062f\u0647 \u0633\u0627\u0632\u06cc pdf \u0646\u0648\u0627\u0646\u062f\u06cc\u0634\u0627\u0646", None))
        self.lbl_logo.setText("")
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle(QCoreApplication.translate("mainWindow", u"\u062a\u0646\u0638\u06cc\u0645\u0627\u062a", None))
        self.groupBox_5.setTitle("")
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\u0631\u0632\u0648\u0644\u0648\u0634\u0646 \u062a\u0635\u0627\u0648\u06cc\u0631 \u0631\u0646\u06af\u06cc", None))
        self.groupBox_6.setTitle("")
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\u0631\u0632\u0648\u0644\u0648\u0634\u0646 \u062a\u0635\u0627\u0648\u06cc\u0631 \u06cc\u0627\u0647 \u0633\u0641\u06cc\u062f", None))
        self.groupBox_7.setTitle("")
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"\u0631\u0632\u0648\u0644\u0648\u0634\u0646 \u062a\u0635\u0627\u0648\u06cc\u0631 \u0645\u0648\u0646\u0648", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("mainWindow", u"\u0641\u0627\u06cc\u0644", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("mainWindow", u"\u0628\u0627\u0632\u06a9\u0631\u062f\u0646", None))
        self.btn_openfile.setText(QCoreApplication.translate("mainWindow", u"\u0628\u0627\u0632 \u06a9\u0631\u062f\u0646 \u0641\u0627\u06cc\u0644", None))
        self.btn_convert.setText(QCoreApplication.translate("mainWindow", u"\u062a\u0628\u062f\u06cc\u0644", None))
        self.btn_savefile.setText(QCoreApplication.translate("mainWindow", u"\u0630\u062e\u06cc\u0631\u0647", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("mainWindow", u"\u0645\u0634\u062e\u0635\u0627\u062a", None))
        self.groupBox_12.setTitle("")
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"\u062d\u062c\u0645:", None))
        self.lbl_file_size.setText("")
        self.groupBox_11.setTitle("")
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"\u0646\u0627\u0645:", None))
        self.lbl_file_name.setText("")
        self.groupBox_10.setTitle("")
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"\u062d\u062c\u0645 \u0628\u0639\u062f \u0627\u0632 \u062a\u0628\u062f\u06cc\u0644:", None))
        self.lbl_file_after_size.setText("")
        self.menu.setTitle(QCoreApplication.translate("mainWindow", u"\u0641\u0627\u06cc\u0644", None))
    # retranslateUi

