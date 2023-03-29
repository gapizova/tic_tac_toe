# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon,
                           QPixmap)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QTabWidget, QVBoxLayout, QWidget)


import r


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 400)
        MainWindow.setMinimumSize(QSize(700, 400))
        MainWindow.setMaximumSize(QSize(700, 400))
        icon = QIcon()
        icon.addFile(u":/images/resource/images/title_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-image: url(:/images/resource/images/bg.png);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(700, 400))
        self.centralwidget.setMaximumSize(QSize(700, 400))
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/images/resource/images/name.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_x = QPushButton(self.centralwidget)
        self.btn_x.setObjectName(u"btn_x")
        self.btn_x.setMinimumSize(QSize(0, 34))
        self.btn_x.setStyleSheet(u"QPushButton{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(45, 45, 45, 255), stop:1 rgba(68, 68, 68, 255));\n"
                                 "background-image: url(:/images/resource/images/cross_small.png);\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-position: center center;\n"
                                 "border: 1px solid #333;\n"
                                 "border-top-left-radius: 5px;\n"
                                 "border-bottom-left-radius: 5px;\n"
                                 "}\n"
                                 "QPushButton::hover{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(66, 66, 66, 255), stop:1 rgba(106, 106, 106, 255));\n"
                                 "}\n"
                                 "QPushButton::pressed{\n"
                                 "background-color: rgb(58, 58, 58);\n"
                                 "}")

        self.horizontalLayout.addWidget(self.btn_x)

        self.btn_o = QPushButton(self.centralwidget)
        self.btn_o.setObjectName(u"btn_o")
        self.btn_o.setMinimumSize(QSize(0, 34))
        self.btn_o.setStyleSheet(u"QPushButton{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(45, 45, 45, 255), stop:1 rgba(68, 68, 68, 255));\n"
                                 "background-image: url(:/images/resource/images/zero_small.png);\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-position: center center;\n"
                                 "border: 1px solid #333;\n"
                                 "border-left: none;\n"
                                 "border-top-right-radius: 5px;\n"
                                 "border-bottom-right-radius: 5px;\n"
                                 "}\n"
                                 "QPushButton::hover{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(66, 66, 66, 255), stop:1 rgba(106, 106, 106, 255));\n"
                                 "}\n"
                                 "QPushButton::pressed{\n"
                                 "background-color: rgb(58, 58, 58);\n"
                                 "}")

        self.horizontalLayout.addWidget(self.btn_o)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_status = QLabel(self.centralwidget)
        self.lbl_status.setObjectName(u"lbl_status")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_status.sizePolicy().hasHeightForWidth())
        self.lbl_status.setSizePolicy(sizePolicy)
        self.lbl_status.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Roboto Medium"])
        font.setPointSize(16)
        self.lbl_status.setFont(font)
        self.lbl_status.setStyleSheet(u"background: none;")
        self.lbl_status.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_status)

        self.btn_play = QPushButton(self.centralwidget)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMinimumSize(QSize(0, 38))
        self.btn_play.setStyleSheet(u"QPushButton{\n"
                                    "color: white;\n"
                                    "background: none;\n"
                                    "border: none;\n"
                                    "border-radius: 19px;\n"
                                    "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(43, 54, 232, 255), stop:1 rgba(0, 108, 237, 255));\n"
                                    "font: 57 16pt \"Roboto Medium\";\n"
                                    "}\n"
                                    "QPushButton::hover{\n"
                                    "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(83, 92, 232, 255), stop:1 rgba(75, 149, 237, 255));\n"
                                    "}\n"
                                    "QPushButton::pressed{\n"
                                    "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(14, 27, 232, 255), stop:1 rgba(49, 98, 156, 255));\n"
                                    "}")

        self.verticalLayout.addWidget(self.btn_play)

        self.btn_info = QPushButton(self.centralwidget)
        self.btn_info.setObjectName(u"btn_info")
        self.btn_info.setMinimumSize(QSize(0, 38))
        self.btn_info.setStyleSheet(u"QPushButton{\n"
                                    "color: white;\n"
                                    "background: none;\n"
                                    "border: none;\n"
                                    "border-radius: 19px;\n"
                                    "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(43, 54, 232, 255), stop:1 rgba(0, 108, 237, 255));\n"
                                    "font: 57 16pt \"Roboto Medium\";\n"
                                    "}\n"
                                    "QPushButton::hover{\n"
                                    "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(83, 92, 232, 255), stop:1 rgba(75, 149, 237, 255));\n"
                                    "}\n"
                                    "QPushButton::pressed{\n"
                                    "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(14, 27, 232, 255), stop:1 rgba(49, 98, 156, 255));\n"
                                    "}")

        self.verticalLayout.addWidget(self.btn_info)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMaximumSize(QSize(325, 320))
        self.tabWidget.setBaseSize(QSize(2, 0))
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setStyleSheet(u"QTabWidget{\n"
                                     "border:none;\n"
                                     "}\n"
                                     "QTabWidget::pane{\n"
                                     "border: 1px solid #222;\n"
                                     "border-radius:3px;\n"
                                     "}\n"
                                     "QWidget#tab_play{\n"
                                     "background: rgb(37, 40, 52);\n"
                                     "}")
        self.tabWidget.setTabBarAutoHide(True)
        self.tab_play = QWidget()
        self.tab_play.setObjectName(u"tab_play")
        self.gridLayout = QGridLayout(self.tab_play)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.btn_0_0 = QPushButton(self.tab_play)
        self.btn_0_0.setObjectName(u"btn_0_0")
        sizePolicy1.setHeightForWidth(self.btn_0_0.sizePolicy().hasHeightForWidth())
        self.btn_0_0.setSizePolicy(sizePolicy1)
        self.btn_0_0.setMinimumSize(QSize(100, 100))
        self.btn_0_0.setBaseSize(QSize(0, 0))
        self.btn_0_0.setStyleSheet(u"QPushButton{\n"
                                   "border:none;\n"
                                   "background:rgb(37, 35, 49);\n"
                                   "}\n"
                                   "QPushButton::hover{\n"
                                   "background: rgb(49, 53, 65);\n"
                                   "}\n"
                                   "QPushButton::pressed{\n"
                                   "background: rgb(83, 83, 83);\n"
                                   "}")

        self.gridLayout.addWidget(self.btn_0_0, 0, 0, 1, 1)

        self.btn_0_1 = QPushButton(self.tab_play)
        self.btn_0_1.setObjectName(u"btn_0_1")
        sizePolicy1.setHeightForWidth(self.btn_0_1.sizePolicy().hasHeightForWidth())
        self.btn_0_1.setSizePolicy(sizePolicy1)
        self.btn_0_1.setMinimumSize(QSize(100, 100))
        self.btn_0_1.setStyleSheet(u"QPushButton{\n"
                                   "border:none;\n"
                                   "background:rgb(37, 35, 49);\n"
                                   "}\n"
                                   "QPushButton::hover{\n"
                                   "background: rgb(49, 53, 65);\n"
                                   "}\n"
                                   "QPushButton::pressed{\n"
                                   "background: rgb(83, 83, 83);\n"
                                   "}")

        self.gridLayout.addWidget(self.btn_0_1, 0, 1, 1, 1)

        self.btn_0_2 = QPushButton(self.tab_play)
        self.btn_0_2.setObjectName(u"btn_0_2")
        sizePolicy1.setHeightForWidth(self.btn_0_2.sizePolicy().hasHeightForWidth())
        self.btn_0_2.setSizePolicy(sizePolicy1)
        self.btn_0_2.setMinimumSize(QSize(100, 100))
        self.btn_0_2.setStyleSheet(u"QPushButton{\n"
                                   "border:none;\n"
                                   "background:rgb(37, 35, 49);\n"
                                   "}\n"
                                   "QPushButton::hover{\n"
                                   "background: rgb(49, 53, 65);\n"
                                   "}\n"
                                   "QPushButton::pressed{\n"
                                   "background: rgb(83, 83, 83);\n"
                                   "}")

        self.gridLayout.addWidget(self.btn_0_2, 0, 2, 1, 1)

        self.btn_1_0 = QPushButton(self.tab_play)
        self.btn_1_0.setObjectName(u"btn_1_0")
        sizePolicy1.setHeightForWidth(self.btn_1_0.sizePolicy().hasHeightForWidth())
        self.btn_1_0.setSizePolicy(sizePolicy1)
        self.btn_1_0.setMinimumSize(QSize(100, 100))
        self.btn_1_0.setStyleSheet(u"QPushButton{\n"
                                   "border:none;\n"
                                   "background:rgb(37, 35, 49);\n"
                                   "}\n"
                                   "QPushButton::hover{\n"
                                   "background: rgb(49, 53, 65);\n"
                                   "}\n"
                                   "QPushButton::pressed{\n"
                                   "background: rgb(83, 83, 83);\n"
                                   "}")

        self.gridLayout.addWidget(self.btn_1_0, 1, 0, 1, 1)

        self.btn_1_1 = QPushButton(self.tab_play)
        self.btn_1_1.setObjectName(u"btn_1_1")
        sizePolicy1.setHeightForWidth(self.btn_1_1.sizePolicy().hasHeightForWidth())
        self.btn_1_1.setSizePolicy(sizePolicy1)
        self.btn_1_1.setMinimumSize(QSize(100, 100))
        self.btn_1_1.setStyleSheet(u"QPushButton{\n"
                                   "border:none;\n"
                                   "background:rgb(37, 35, 49);\n"
                                   "}\n"
                                   "QPushButton::hover{\n"
                                   "background: rgb(49, 53, 65);\n"
                                   "}\n"
                                   "QPushButton::pressed{\n"
                                   "background: rgb(83, 83, 83);\n"
                                   "}")

        self.gridLayout.addWidget(self.btn_1_1, 1, 1, 1, 1)

        self.btn_1_2 = QPushButton(self.tab_play)
        self.btn_1_2.setObjectName(u"btn_1_2")
        sizePolicy1.setHeightForWidth(self.btn_1_2.sizePolicy().hasHeightForWidth())
        self.btn_1_2.setSizePolicy(sizePolicy1)
        self.btn_1_2.setMinimumSize(QSize(100, 100))
        self.btn_1_2.setStyleSheet(u"QPushButton{\n"
                                   "border:none;\n"
                                   "background:rgb(37, 35, 49);\n"
                                   "}\n"
                                   "QPushButton::hover{\n"
                                   "background: rgb(49, 53, 65);\n"
                                   "}\n"
                                   "QPushButton::pressed{\n"
                                   "background: rgb(83, 83, 83);\n"
                                   "}")

        self.gridLayout.addWidget(self.btn_1_2, 1, 2, 1, 1)

        self.btn_2_0 = QPushButton(self.tab_play)
        self.btn_2_0.setObjectName(u"btn_2_0")
        sizePolicy1.setHeightForWidth(self.btn_2_0.sizePolicy().hasHeightForWidth())
        self.btn_2_0.setSizePolicy(sizePolicy1)
        self.btn_2_0.setMinimumSize(QSize(100, 100))
        self.btn_2_0.setStyleSheet(u"QPushButton{\n"
                                   "border:none;\n"
                                   "background:rgb(37, 35, 49);\n"
                                   "}\n"
                                   "QPushButton::hover{\n"
                                   "background: rgb(49, 53, 65);\n"
                                   "}\n"
                                   "QPushButton::pressed{\n"
                                   "background: rgb(83, 83, 83);\n"
                                   "}")

        self.gridLayout.addWidget(self.btn_2_0, 2, 0, 1, 1)

        self.btn_2_1 = QPushButton(self.tab_play)
        self.btn_2_1.setObjectName(u"btn_2_1")
        sizePolicy1.setHeightForWidth(self.btn_2_1.sizePolicy().hasHeightForWidth())
        self.btn_2_1.setSizePolicy(sizePolicy1)
        self.btn_2_1.setMinimumSize(QSize(100, 100))
        self.btn_2_1.setStyleSheet(u"QPushButton{\n"
                                   "border:none;\n"
                                   "background:rgb(37, 35, 49);\n"
                                   "}\n"
                                   "QPushButton::hover{\n"
                                   "background: rgb(49, 53, 65);\n"
                                   "}\n"
                                   "QPushButton::pressed{\n"
                                   "background: rgb(83, 83, 83);\n"
                                   "}")

        self.gridLayout.addWidget(self.btn_2_1, 2, 1, 1, 1)

        self.btn_2_2 = QPushButton(self.tab_play)
        self.btn_2_2.setObjectName(u"btn_2_2")
        sizePolicy1.setHeightForWidth(self.btn_2_2.sizePolicy().hasHeightForWidth())
        self.btn_2_2.setSizePolicy(sizePolicy1)
        self.btn_2_2.setMinimumSize(QSize(100, 100))
        self.btn_2_2.setStyleSheet(u"QPushButton{\n"
                                   "border:none;\n"
                                   "background:rgb(37, 35, 49);\n"
                                   "}\n"
                                   "QPushButton::hover{\n"
                                   "background: rgb(49, 53, 65);\n"
                                   "}\n"
                                   "QPushButton::pressed{\n"
                                   "background: rgb(83, 83, 83);\n"
                                   "}")

        self.gridLayout.addWidget(self.btn_2_2, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_play, "")
        self.tab_info = QWidget()
        self.tab_info.setObjectName(u"tab_info")
        self.verticalLayout_2 = QVBoxLayout(self.tab_info)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_info = QLabel(self.tab_info)
        self.lbl_info.setObjectName(u"lbl_info")
        self.lbl_info.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.lbl_info.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lbl_info)

        self.tabWidget.addTab(self.tab_info, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u041a\u0440\u0435\u0441\u0442\u0438\u043a\u0438 - \u041d\u043e\u043b\u0438\u043a\u0438",
                                                             None))
        self.label.setText("")
        self.btn_x.setText("")
        self.btn_o.setText("")
        self.btn_play.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c", None))
        self.btn_info.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431 \u0438\u0433\u0440\u0435", None))
        # if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.btn_0_0.setText("")
        self.btn_0_1.setText("")
        self.btn_0_2.setText("")
        self.btn_1_0.setText("")
        self.btn_1_1.setText("")
        self.btn_1_2.setText("")
        self.btn_2_0.setText("")
        self.btn_2_1.setText("")
        self.btn_2_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_play), "")
        self.lbl_info.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_info), "")
    # retranslateUi
