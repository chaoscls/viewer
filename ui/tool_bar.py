# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tool_bar.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(396, 868)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_tool_bar = QVBoxLayout()
        self.verticalLayout_tool_bar.setObjectName(u"verticalLayout_tool_bar")
        self.verticalLayout_volume = QVBoxLayout()
        self.verticalLayout_volume.setObjectName(u"verticalLayout_volume")
        self.label_volume = QLabel(Form)
        self.label_volume.setObjectName(u"label_volume")

        self.verticalLayout_volume.addWidget(self.label_volume)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_volume.addWidget(self.pushButton)

        self.horizontalLayout_min = QHBoxLayout()
        self.horizontalLayout_min.setObjectName(u"horizontalLayout_min")
        self.label_min = QLabel(Form)
        self.label_min.setObjectName(u"label_min")
        font = QFont()
        font.setPointSize(11)
        self.label_min.setFont(font)

        self.horizontalLayout_min.addWidget(self.label_min)

        self.horizontalSlider_min = QSlider(Form)
        self.horizontalSlider_min.setObjectName(u"horizontalSlider_min")
        self.horizontalSlider_min.setEnabled(False)
        self.horizontalSlider_min.setOrientation(Qt.Horizontal)

        self.horizontalLayout_min.addWidget(self.horizontalSlider_min)

        self.label_min_value = QLabel(Form)
        self.label_min_value.setObjectName(u"label_min_value")
        self.label_min_value.setMinimumSize(QSize(45, 20))
        self.label_min_value.setMaximumSize(QSize(45, 20))
        self.label_min_value.setFont(font)
        self.label_min_value.setLineWidth(1)
        self.label_min_value.setMargin(4)
        self.label_min_value.setIndent(4)

        self.horizontalLayout_min.addWidget(self.label_min_value)

        self.horizontalLayout_min.setStretch(1, 1)

        self.verticalLayout_volume.addLayout(self.horizontalLayout_min)

        self.horizontalLayout_max = QHBoxLayout()
        self.horizontalLayout_max.setObjectName(u"horizontalLayout_max")
        self.label_max = QLabel(Form)
        self.label_max.setObjectName(u"label_max")
        self.label_max.setFont(font)

        self.horizontalLayout_max.addWidget(self.label_max)

        self.horizontalSlider_max = QSlider(Form)
        self.horizontalSlider_max.setObjectName(u"horizontalSlider_max")
        self.horizontalSlider_max.setEnabled(False)
        self.horizontalSlider_max.setOrientation(Qt.Horizontal)

        self.horizontalLayout_max.addWidget(self.horizontalSlider_max)

        self.label_max_value = QLabel(Form)
        self.label_max_value.setObjectName(u"label_max_value")
        self.label_max_value.setMinimumSize(QSize(45, 20))
        self.label_max_value.setMaximumSize(QSize(45, 20))
        self.label_max_value.setFont(font)
        self.label_max_value.setMargin(4)
        self.label_max_value.setIndent(4)

        self.horizontalLayout_max.addWidget(self.label_max_value)


        self.verticalLayout_volume.addLayout(self.horizontalLayout_max)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_volume.addWidget(self.line)

        self.verticalSpacer_volume = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_volume.addItem(self.verticalSpacer_volume)


        self.verticalLayout_tool_bar.addLayout(self.verticalLayout_volume)

        self.verticalLayout_seg = QVBoxLayout()
        self.verticalLayout_seg.setObjectName(u"verticalLayout_seg")
        self.horizontalLayout_seg_check = QHBoxLayout()
        self.horizontalLayout_seg_check.setObjectName(u"horizontalLayout_seg_check")
        self.label_seg = QLabel(Form)
        self.label_seg.setObjectName(u"label_seg")

        self.horizontalLayout_seg_check.addWidget(self.label_seg)

        self.horizontalLayout_seg_check.setStretch(0, 1)

        self.verticalLayout_seg.addLayout(self.horizontalLayout_seg_check)

        self.pushButton_seg = QPushButton(Form)
        self.pushButton_seg.setObjectName(u"pushButton_seg")

        self.verticalLayout_seg.addWidget(self.pushButton_seg)

        self.horizontalLayout_seg_opacity = QHBoxLayout()
        self.horizontalLayout_seg_opacity.setObjectName(u"horizontalLayout_seg_opacity")
        self.label_seg_opacity = QLabel(Form)
        self.label_seg_opacity.setObjectName(u"label_seg_opacity")
        self.label_seg_opacity.setFont(font)

        self.horizontalLayout_seg_opacity.addWidget(self.label_seg_opacity)

        self.horizontalSlider_seg = QSlider(Form)
        self.horizontalSlider_seg.setObjectName(u"horizontalSlider_seg")
        self.horizontalSlider_seg.setEnabled(False)
        self.horizontalSlider_seg.setFont(font)
        self.horizontalSlider_seg.setMaximum(100)
        self.horizontalSlider_seg.setSingleStep(1)
        self.horizontalSlider_seg.setPageStep(10)
        self.horizontalSlider_seg.setOrientation(Qt.Horizontal)

        self.horizontalLayout_seg_opacity.addWidget(self.horizontalSlider_seg)

        self.label_seg_opacity_value = QLabel(Form)
        self.label_seg_opacity_value.setObjectName(u"label_seg_opacity_value")
        self.label_seg_opacity_value.setFont(font)

        self.horizontalLayout_seg_opacity.addWidget(self.label_seg_opacity_value)

        self.checkBox_seg = QCheckBox(Form)
        self.checkBox_seg.setObjectName(u"checkBox_seg")
        self.checkBox_seg.setEnabled(False)

        self.horizontalLayout_seg_opacity.addWidget(self.checkBox_seg)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_seg_opacity.addItem(self.horizontalSpacer)

        self.horizontalLayout_seg_opacity.setStretch(1, 5)

        self.verticalLayout_seg.addLayout(self.horizontalLayout_seg_opacity)

        self.verticalSpacer_seg = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_seg.addItem(self.verticalSpacer_seg)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_seg.addWidget(self.line_2)


        self.verticalLayout_tool_bar.addLayout(self.verticalLayout_seg)

        self.verticalLayout_logits = QVBoxLayout()
        self.verticalLayout_logits.setObjectName(u"verticalLayout_logits")
        self.horizontalLayout_logits_check = QHBoxLayout()
        self.horizontalLayout_logits_check.setObjectName(u"horizontalLayout_logits_check")
        self.label_logits = QLabel(Form)
        self.label_logits.setObjectName(u"label_logits")

        self.horizontalLayout_logits_check.addWidget(self.label_logits)

        self.comboBox_logits_style = QComboBox(Form)
        self.comboBox_logits_style.addItem("")
        self.comboBox_logits_style.addItem("")
        self.comboBox_logits_style.setObjectName(u"comboBox_logits_style")
        self.comboBox_logits_style.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_logits_check.addWidget(self.comboBox_logits_style)

        self.horizontalLayout_logits_check.setStretch(0, 1)

        self.verticalLayout_logits.addLayout(self.horizontalLayout_logits_check)

        self.pushButton_logits = QPushButton(Form)
        self.pushButton_logits.setObjectName(u"pushButton_logits")

        self.verticalLayout_logits.addWidget(self.pushButton_logits)

        self.comboBox_logits = QComboBox(Form)
        self.comboBox_logits.setObjectName(u"comboBox_logits")
        self.comboBox_logits.setEnabled(False)

        self.verticalLayout_logits.addWidget(self.comboBox_logits)

        self.horizontalLayout_logits_opacity = QHBoxLayout()
        self.horizontalLayout_logits_opacity.setObjectName(u"horizontalLayout_logits_opacity")
        self.label_logits_opacity = QLabel(Form)
        self.label_logits_opacity.setObjectName(u"label_logits_opacity")
        self.label_logits_opacity.setMinimumSize(QSize(40, 0))
        self.label_logits_opacity.setFont(font)

        self.horizontalLayout_logits_opacity.addWidget(self.label_logits_opacity)

        self.horizontalSlider_logits = QSlider(Form)
        self.horizontalSlider_logits.setObjectName(u"horizontalSlider_logits")
        self.horizontalSlider_logits.setEnabled(False)
        self.horizontalSlider_logits.setOrientation(Qt.Horizontal)

        self.horizontalLayout_logits_opacity.addWidget(self.horizontalSlider_logits)

        self.label_logits_opacity_value = QLabel(Form)
        self.label_logits_opacity_value.setObjectName(u"label_logits_opacity_value")
        self.label_logits_opacity_value.setFont(font)

        self.horizontalLayout_logits_opacity.addWidget(self.label_logits_opacity_value)

        self.checkBox_logits = QCheckBox(Form)
        self.checkBox_logits.setObjectName(u"checkBox_logits")
        self.checkBox_logits.setEnabled(False)

        self.horizontalLayout_logits_opacity.addWidget(self.checkBox_logits)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_logits_opacity.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_logits_opacity.setStretch(1, 1)

        self.verticalLayout_logits.addLayout(self.horizontalLayout_logits_opacity)

        self.verticalLayout_logits_left_threshold = QVBoxLayout()
        self.verticalLayout_logits_left_threshold.setObjectName(u"verticalLayout_logits_left_threshold")
        self.line_5 = QFrame(Form)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_logits_left_threshold.addWidget(self.line_5)

        self.label_left_logits = QLabel(Form)
        self.label_left_logits.setObjectName(u"label_left_logits")

        self.verticalLayout_logits_left_threshold.addWidget(self.label_left_logits)

        self.horizontalLayout_logits_left_low = QHBoxLayout()
        self.horizontalLayout_logits_left_low.setObjectName(u"horizontalLayout_logits_left_low")
        self.label_logits_left_low = QLabel(Form)
        self.label_logits_left_low.setObjectName(u"label_logits_left_low")
        self.label_logits_left_low.setMinimumSize(QSize(40, 0))
        self.label_logits_left_low.setFont(font)

        self.horizontalLayout_logits_left_low.addWidget(self.label_logits_left_low)

        self.horizontalSlider_logits_left_low = QSlider(Form)
        self.horizontalSlider_logits_left_low.setObjectName(u"horizontalSlider_logits_left_low")
        self.horizontalSlider_logits_left_low.setEnabled(False)
        self.horizontalSlider_logits_left_low.setOrientation(Qt.Horizontal)

        self.horizontalLayout_logits_left_low.addWidget(self.horizontalSlider_logits_left_low)

        self.spinBox_logits_left_low_value = QSpinBox(Form)
        self.spinBox_logits_left_low_value.setObjectName(u"spinBox_logits_left_low_value")
        self.spinBox_logits_left_low_value.setEnabled(False)
        self.spinBox_logits_left_low_value.setMinimum(0)

        self.horizontalLayout_logits_left_low.addWidget(self.spinBox_logits_left_low_value)

        self.horizontalLayout_logits_left_low.setStretch(1, 1)

        self.verticalLayout_logits_left_threshold.addLayout(self.horizontalLayout_logits_left_low)

        self.horizontalLayout_logits_left_high = QHBoxLayout()
        self.horizontalLayout_logits_left_high.setObjectName(u"horizontalLayout_logits_left_high")
        self.label_logits_left_high = QLabel(Form)
        self.label_logits_left_high.setObjectName(u"label_logits_left_high")
        self.label_logits_left_high.setMinimumSize(QSize(40, 0))
        self.label_logits_left_high.setFont(font)

        self.horizontalLayout_logits_left_high.addWidget(self.label_logits_left_high)

        self.horizontalSlider_logits_left_high = QSlider(Form)
        self.horizontalSlider_logits_left_high.setObjectName(u"horizontalSlider_logits_left_high")
        self.horizontalSlider_logits_left_high.setEnabled(False)
        self.horizontalSlider_logits_left_high.setOrientation(Qt.Horizontal)

        self.horizontalLayout_logits_left_high.addWidget(self.horizontalSlider_logits_left_high)

        self.spinBox_logits_left_high_value = QSpinBox(Form)
        self.spinBox_logits_left_high_value.setObjectName(u"spinBox_logits_left_high_value")
        self.spinBox_logits_left_high_value.setEnabled(False)
        self.spinBox_logits_left_high_value.setMinimum(0)

        self.horizontalLayout_logits_left_high.addWidget(self.spinBox_logits_left_high_value)

        self.horizontalLayout_logits_left_high.setStretch(1, 1)

        self.verticalLayout_logits_left_threshold.addLayout(self.horizontalLayout_logits_left_high)


        self.verticalLayout_logits.addLayout(self.verticalLayout_logits_left_threshold)

        self.verticalLayout_logits_right_threshold = QVBoxLayout()
        self.verticalLayout_logits_right_threshold.setObjectName(u"verticalLayout_logits_right_threshold")
        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_logits_right_threshold.addWidget(self.line_4)

        self.label_right_logits = QLabel(Form)
        self.label_right_logits.setObjectName(u"label_right_logits")

        self.verticalLayout_logits_right_threshold.addWidget(self.label_right_logits)

        self.horizontalLayout_logits_right_low = QHBoxLayout()
        self.horizontalLayout_logits_right_low.setObjectName(u"horizontalLayout_logits_right_low")
        self.label_logits_right_low = QLabel(Form)
        self.label_logits_right_low.setObjectName(u"label_logits_right_low")
        self.label_logits_right_low.setMinimumSize(QSize(40, 0))
        self.label_logits_right_low.setFont(font)

        self.horizontalLayout_logits_right_low.addWidget(self.label_logits_right_low)

        self.horizontalSlider_logits_right_low = QSlider(Form)
        self.horizontalSlider_logits_right_low.setObjectName(u"horizontalSlider_logits_right_low")
        self.horizontalSlider_logits_right_low.setEnabled(False)
        self.horizontalSlider_logits_right_low.setMinimum(0)
        self.horizontalSlider_logits_right_low.setOrientation(Qt.Horizontal)

        self.horizontalLayout_logits_right_low.addWidget(self.horizontalSlider_logits_right_low)

        self.spinBox_logits_right_low_value = QSpinBox(Form)
        self.spinBox_logits_right_low_value.setObjectName(u"spinBox_logits_right_low_value")
        self.spinBox_logits_right_low_value.setEnabled(False)
        self.spinBox_logits_right_low_value.setMinimum(0)

        self.horizontalLayout_logits_right_low.addWidget(self.spinBox_logits_right_low_value)


        self.verticalLayout_logits_right_threshold.addLayout(self.horizontalLayout_logits_right_low)

        self.horizontalLayout_logits_right_high = QHBoxLayout()
        self.horizontalLayout_logits_right_high.setObjectName(u"horizontalLayout_logits_right_high")
        self.label_logits_right_high = QLabel(Form)
        self.label_logits_right_high.setObjectName(u"label_logits_right_high")
        self.label_logits_right_high.setMinimumSize(QSize(40, 0))
        self.label_logits_right_high.setFont(font)

        self.horizontalLayout_logits_right_high.addWidget(self.label_logits_right_high)

        self.horizontalSlider_logits_right_high = QSlider(Form)
        self.horizontalSlider_logits_right_high.setObjectName(u"horizontalSlider_logits_right_high")
        self.horizontalSlider_logits_right_high.setEnabled(False)
        self.horizontalSlider_logits_right_high.setOrientation(Qt.Horizontal)

        self.horizontalLayout_logits_right_high.addWidget(self.horizontalSlider_logits_right_high)

        self.spinBox_logits_right_high_value = QSpinBox(Form)
        self.spinBox_logits_right_high_value.setObjectName(u"spinBox_logits_right_high_value")
        self.spinBox_logits_right_high_value.setEnabled(False)

        self.horizontalLayout_logits_right_high.addWidget(self.spinBox_logits_right_high_value)

        self.horizontalLayout_logits_right_high.setStretch(1, 1)

        self.verticalLayout_logits_right_threshold.addLayout(self.horizontalLayout_logits_right_high)


        self.verticalLayout_logits.addLayout(self.verticalLayout_logits_right_threshold)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_logits.addWidget(self.line_3)


        self.verticalLayout_tool_bar.addLayout(self.verticalLayout_logits)

        self.verticalLayout_property = QVBoxLayout()
        self.verticalLayout_property.setObjectName(u"verticalLayout_property")
        self.label_property = QLabel(Form)
        self.label_property.setObjectName(u"label_property")
        self.label_property.setMinimumSize(QSize(0, 30))

        self.verticalLayout_property.addWidget(self.label_property)

        self.verticalSpacer_logits = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_property.addItem(self.verticalSpacer_logits)


        self.verticalLayout_tool_bar.addLayout(self.verticalLayout_property)

        self.verticalLayout_tool_bar.setStretch(3, 1)

        self.verticalLayout.addLayout(self.verticalLayout_tool_bar)


        self.retranslateUi(Form)
        self.horizontalSlider_seg.valueChanged.connect(self.label_seg_opacity_value.setNum)
        self.horizontalSlider_logits.valueChanged.connect(self.label_logits_opacity_value.setNum)
        self.horizontalSlider_max.valueChanged.connect(self.label_max_value.setNum)
        self.horizontalSlider_min.valueChanged.connect(self.label_min_value.setNum)
        self.horizontalSlider_logits_left_high.valueChanged.connect(self.spinBox_logits_left_high_value.setValue)
        self.horizontalSlider_logits_left_low.valueChanged.connect(self.spinBox_logits_left_low_value.setValue)
        self.horizontalSlider_logits_right_low.valueChanged.connect(self.spinBox_logits_right_low_value.setValue)
        self.horizontalSlider_logits_right_high.valueChanged.connect(self.spinBox_logits_right_high_value.setValue)
        self.spinBox_logits_left_high_value.valueChanged.connect(self.horizontalSlider_logits_left_high.setValue)
        self.spinBox_logits_left_low_value.valueChanged.connect(self.horizontalSlider_logits_left_low.setValue)
        self.spinBox_logits_right_high_value.valueChanged.connect(self.horizontalSlider_logits_right_high.setValue)
        self.spinBox_logits_right_low_value.valueChanged.connect(self.horizontalSlider_logits_right_low.setValue)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Viewer", None))
        self.label_volume.setText(QCoreApplication.translate("Form", u"Volume", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Open", None))
        self.label_min.setText(QCoreApplication.translate("Form", u"Min", None))
        self.label_min_value.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_max.setText(QCoreApplication.translate("Form", u"Max", None))
#if QT_CONFIG(tooltip)
        self.horizontalSlider_max.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_max_value.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_seg.setText(QCoreApplication.translate("Form", u"Segmentation", None))
        self.pushButton_seg.setText(QCoreApplication.translate("Form", u"Open", None))
        self.label_seg_opacity.setText(QCoreApplication.translate("Form", u"Opacity", None))
        self.label_seg_opacity_value.setText(QCoreApplication.translate("Form", u"0", None))
        self.checkBox_seg.setText("")
        self.label_logits.setText(QCoreApplication.translate("Form", u"Logits", None))
        self.comboBox_logits_style.setItemText(0, QCoreApplication.translate("Form", u"JET", None))
        self.comboBox_logits_style.setItemText(1, QCoreApplication.translate("Form", u"NONE", None))

        self.pushButton_logits.setText(QCoreApplication.translate("Form", u"Open", None))
        self.label_logits_opacity.setText(QCoreApplication.translate("Form", u"Opacity", None))
        self.label_logits_opacity_value.setText(QCoreApplication.translate("Form", u"0", None))
        self.checkBox_logits.setText("")
        self.label_left_logits.setText(QCoreApplication.translate("Form", u"Left", None))
        self.label_logits_left_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.label_logits_left_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.label_right_logits.setText(QCoreApplication.translate("Form", u"Right", None))
        self.label_logits_right_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.label_logits_right_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.label_property.setText("")
    # retranslateUi

