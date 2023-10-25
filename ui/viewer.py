# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QScrollBar, QSizePolicy, QSplitter, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1728, 1051)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_veiw = QVBoxLayout()
        self.verticalLayout_veiw.setObjectName(u"verticalLayout_veiw")
        self.mainScrollBar = QScrollBar(Form)
        self.mainScrollBar.setObjectName(u"mainScrollBar")
        self.mainScrollBar.setOrientation(Qt.Horizontal)

        self.verticalLayout_veiw.addWidget(self.mainScrollBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(2)
        self.graphicsView_left = QGraphicsView(self.splitter)
        self.graphicsView_left.setObjectName(u"graphicsView_left")
        self.splitter.addWidget(self.graphicsView_left)
        self.graphicsView_right = QGraphicsView(self.splitter)
        self.graphicsView_right.setObjectName(u"graphicsView_right")
        self.splitter.addWidget(self.graphicsView_right)

        self.horizontalLayout_2.addWidget(self.splitter)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_veiw.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_veiw)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Viewer", None))
    # retranslateUi

