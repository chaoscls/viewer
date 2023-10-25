from functools import partial
from typing import Optional

import PySide6
from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QGraphicsScene, QSplitter, QTableWidget
from PySide6.QtGui import QPixmap, QImage, QShortcut, QKeySequence, QStandardItemModel
from PySide6.QtCore import Qt, QModelIndex
from PIL import Image, ImageQt
import pandas as pd

from ui import tool_bar, viewer, logits_statistics
from utils.item import *
from utils.datareader import DataReader


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data: pd.DataFrame = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]

            if isinstance(value, (float, np.float32)):
                return "%.3f" % value

            return str(value)

        if role == Qt.BackgroundRole:
            # See below for the data structure.
            if not self._data.values.sum():
                return QtGui.QColor('#202020')
            elif self._data.iloc[index.row(), index.column()] == self._data.iloc[:, index.column()].max():
                return QtGui.QColor('#A52A2A')
            else:
                return QtGui.QColor('#202020')

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def set_data(self, data):
        self.beginResetModel()
        self._data = data
        self.endResetModel()


class Viewer(QWidget, viewer.Ui_Form):

    def __init__(self):
        super(Viewer, self).__init__()
        self.setupUi(self)


class LogitsWindow(QWidget, logits_statistics.Ui_Form):

    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ..., f: PySide6.QtCore.Qt.WindowType = ...) -> None:
        super().__init__()
        self.setupUi(self)

class MainWindow(QWidget, tool_bar.Ui_Form):

    def __init__(self, num_classes=19, dummy_data_size=None):
        super().__init__()
        self.setupUi(self)
        self.viewer = Viewer()
        self.logitsWindow = LogitsWindow()
        self.initial(num_classes, dummy_data_size)
        self.bind()

    def initial(self, num_classes, dummy_data_size):

        self.ratio = 2  # 缩放初始比例
        self.zoom_step = 0.1  # 缩放步长
        self.zoom_max = 10  # 缩放最大值
        self.zoom_min = 0.2  # 缩放最小值
        self.pixmapItem_left = None
        self.pixmapItem_right = None
        self.visible: bool = False

        self.index: int = 0
        self.h: int = 0
        self.w: int = 0
        self.current_cls: int = 0
        self.image: ImageItem = None
        self.seg: SegmentationItem = None
        self.logits_left: LogitsItem = None
        self.logits_right: LogitsItem = None
        self.logits_init: bool = False
        self.logits_opacity: float = 0.5
        self.num_classes: int = num_classes

        if dummy_data_size is not None:
            arr =np.zeros(dummy_data_size)
            self.image = ImageItem(arr, "dummy_data")
            self.index = dummy_data_size[0] - 1
            self.set_image_property()
            self.visible = True

            # if self.viewer.isHidden():
            #     self.viewer.show()
            # self.update_view()

    def bind(self):

        self.scene_left = QGraphicsScene(self)
        self.scene_right = QGraphicsScene(self)

        self.scene_left.mousePressEvent = self.scene_MousePressEvent
        self.scene_left.mouseMoveEvent = self.scene_mouseMoveEvent
        self.scene_left.wheelEvent = self.scene_wheelEvent
        self.scene_left.keyPressEvent = self.keyPressEvent

        self.scene_right.mousePressEvent = self.scene_MousePressEvent
        self.scene_right.mouseMoveEvent = self.scene_mouseMoveEvent
        self.scene_right.wheelEvent = self.scene_wheelEvent
        self.scene_right.keyPressEvent = self.keyPressEvent

        self.viewer.graphicsView_left.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.viewer.graphicsView_left.setSceneRect(0, 0, self.viewer.graphicsView_left.viewport().width(),
                                            self.viewer.graphicsView_left.height())
        self.viewer.graphicsView_left.setScene(self.scene_left)

        self.viewer.graphicsView_right.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.viewer.graphicsView_right.setSceneRect(0, 0, self.viewer.graphicsView_right.viewport().width(),
                                            self.viewer.graphicsView_right.height())
        self.viewer.graphicsView_right.setScene(self.scene_right)

        self.viewer.mainScrollBar.valueChanged.connect(self.depth_scrollbar_handler)

        # Volume
        self.pushButton.clicked.connect(self.open_file)
        self.horizontalSlider_min.valueChanged.connect(self.intensity_slider_handler)
        self.horizontalSlider_max.valueChanged.connect(self.intensity_slider_handler)

        # Segmentation
        self.pushButton_seg.clicked.connect(self.open_seg)
        self.horizontalSlider_seg.valueChanged.connect(self.seg_slider_handler)
        self.checkBox_seg.stateChanged.connect(self.set_seg_visible)

        # Logits
        self.pushButton_logits.clicked.connect(self.open_logits)
        self.horizontalSlider_logits.valueChanged.connect(self.logits_slider_handler)
        self.checkBox_logits.stateChanged.connect(self.set_logits_visible)
        self.comboBox_logits.currentTextChanged.connect(self.set_logits_cls)

        self.horizontalSlider_logits_left_low.valueChanged.connect(self.logits_slider_threshold_handler)
        self.horizontalSlider_logits_left_high.valueChanged.connect(self.logits_slider_threshold_handler)

        self.horizontalSlider_logits_right_low.valueChanged.connect(self.logits_slider_threshold_handler)
        self.horizontalSlider_logits_right_high.valueChanged.connect(self.logits_slider_threshold_handler)

        self.label_property.mouseDoubleClickEvent = self.showLogitsWindow

        self.comboBox_logits_style.currentTextChanged.connect(self.set_logits_style)

        data = pd.DataFrame([[0, 0] for _ in range(self.num_classes)], columns=['Left', 'Right'], index=[str(cls) for cls in range(self.num_classes)])
        self.model = TableModel(data)
        self.logitsWindow.tableView_property.setModel(self.model)

        QShortcut(QKeySequence("Ctrl+w"), self).activated.connect(self.exit_)
        QShortcut(QKeySequence("Ctrl+w"), self.viewer).activated.connect(self.viewer_hide)
        QShortcut(QKeySequence("Ctrl+w"), self.logitsWindow).activated.connect(self.logitsWindow_hide)
        QShortcut(QKeySequence("Ctrl+s"), self).activated.connect(self.show_)

        self.setAcceptDrops(True)
        self.viewer.graphicsView_left.setMouseTracking(True)
        self.viewer.graphicsView_right.setMouseTracking(True)

    def update_view(self):
        if not self.visible:
            return

        view_slide = self.image.arr[self.index]

        im_left = cv2.cvtColor(view_slide, cv2.COLOR_GRAY2RGB)
        im_left = np.float32(im_left) / 255

        if self.seg is not None and self.seg.visible:
            seg = self.seg.rgb[self.index]
            seg = np.float32(seg) / 255
            im_left[seg > 0] = im_left[seg > 0] * self.seg.opacity
            im_left = im_left + seg * (1 - self.seg.opacity)

        im_right = im_left.copy()
        if self.logits_left is not None and self.logits_left.visible:

            logits = self.logits_left.arr[self.index]
            mask = (logits >= self.logits_left.threshold_low) & (logits <= self.logits_left.threshold_high)
            logits_rgb = self.logits_left.rgb[self.index]
            logits_rgb = np.float32(logits_rgb) / 255
            # mask = mask & self.logits_left.mask[self.index]
            im_left[mask] = im_left[mask] * self.logits_opacity
            im_left = im_left + logits_rgb * (1 - self.logits_opacity) * mask[..., None]

        if self.logits_right is not None and self.logits_right.visible:
            logits = self.logits_right.arr[self.index]
            mask = (logits >= self.logits_right.threshold_low) & (logits <= self.logits_right.threshold_high)
            logits_rgb = self.logits_right.rgb[self.index]
            logits_rgb = np.float32(logits_rgb) / 255
            # mask = mask & self.logits_right.mask[self.index]
            im_right[mask] = im_right[mask] * self.logits_opacity
            im_right = im_right + logits_rgb * (1 - self.logits_opacity) * mask[..., None]
            im_right = logits_rgb * mask[..., None]

        im_right = Image.fromarray(np.uint8(255 * im_right))
        im_left = Image.fromarray(np.uint8(255 * im_left))
        self.addScene(im_left, im_right)

    def addScene(self, im_left, im_right):
        if self.pixmapItem_left != None:
            originX = self.pixmapItem_left.x()
            originY = self.pixmapItem_left.y()
        else:
            originX, originY = 0, 0

        self.scene_left.clear()
        self.scene_right.clear()

        self.pixmap_left = ImageQt.toqpixmap(im_left)
        self.pixmapItem_left = self.scene_left.addPixmap(self.pixmap_left)
        self.pixmapItem_left.setScale(self.ratio)
        self.pixmapItem_left.setPos(originX, originY)

        self.pixmap_right = ImageQt.toqpixmap(im_right)
        self.pixmapItem_right = self.scene_right.addPixmap(self.pixmap_right)
        self.pixmapItem_right.setScale(self.ratio)
        self.pixmapItem_right.setPos(originX, originY)

    def update_property(self):
        if not self.visible:
            return
        intensity = ""
        cls = ""
        d, h, w = self.index, self.h, self.w
        if self.image is not None:
            intensity = self.image._arr[d, h, w]
        if self.seg is not None:
            cls = self.seg.arr[d, h, w]
        if self.logits_left is not None:

            logits_left = [logits[d, h, w] for logits in self.logits_left.dict.values()]
            logits_right = [logits[d, h, w] for logits in self.logits_right.dict.values()]
            data = pd.DataFrame(np.array([logits_left, logits_right]).transpose(), columns=['Left', 'Right'],
                                index=[str(cls) for cls in range(self.num_classes)])
            self.model.set_data(data)


        info = f"({h}, {w}, {d}) {intensity}    cls: {cls}"
        self.label_property.setText(info)

    def set_image_property(self):

        self.label_min_value.setText(str(self.image.a_min))
        self.label_max_value.setText(str(self.image.a_max))

        self.viewer.mainScrollBar.setRange(0, self.image.d - 1)
        self.viewer.mainScrollBar.setValue(self.index)

        self.horizontalSlider_min.setRange(self.image.min, self.image.max)
        self.horizontalSlider_min.setValue(self.image.a_min)
        self.horizontalSlider_max.setRange(self.image.min, self.image.max)
        self.horizontalSlider_max.setValue(self.image.a_max)

        self.viewer.mainScrollBar.setEnabled(True)
        self.horizontalSlider_min.setEnabled(True)
        self.horizontalSlider_max.setEnabled(True)


    def open_file(self, file_name: str=None):
        if file_name == None or file_name == False or file_name == "":
            file_name, _ = QFileDialog.getOpenFileName(self, dir="./data", filter="nifty files(*.nii.gz)")
        if file_name == "":
            return
        arr = get_array_from_file(file_name)
        # arr = np.transpose(arr, (2, 1, 0))
        self.image = ImageItem(arr, file_name)
        self.index = arr.shape[0] - 1
        self.set_image_property()
        self.visible = True

        if self.viewer.isHidden():
            self.viewer.show()
        self.update_view()

    def open_seg(self, file_name: str=None):
        if file_name == None or file_name == False or file_name == "":
            file_name, _ = QFileDialog.getOpenFileName(self, dir="./data", filter="nifty files(*.nii.gz)")
        if file_name == "":
            return
        arr = get_array_from_file(file_name)
        self.seg = SegmentationItem(arr, file_name)

        self.horizontalSlider_seg.setEnabled(True)
        self.checkBox_seg.setEnabled(True)
        self.checkBox_seg.setChecked(True)
        self.horizontalSlider_seg.setValue(int(self.seg.opacity * 100))

        self.update_view()

    def open_logits(self, file_name=None, pos="left"):

        def setup_left_logits(arr, file_name):
            if self.logits_left is None:
                self.horizontalSlider_logits_left_low.setEnabled(True)
                self.horizontalSlider_logits_left_high.setEnabled(True)
                self.spinBox_logits_left_low_value.setEnabled(True)
                self.spinBox_logits_left_high_value.setEnabled(True)
            self.logits_left = LogitsItem(arr, file_name)
            self.label_left_logits.setText(self.logits_left.second_name)

        def setup_right_logits(arr, file_name):
            if self.logits_right is None:
                self.horizontalSlider_logits_right_low.setEnabled(True)
                self.horizontalSlider_logits_right_high.setEnabled(True)
                self.spinBox_logits_right_low_value.setEnabled(True)
                self.spinBox_logits_right_high_value.setEnabled(True)
            self.logits_right = LogitsItem(arr, file_name)
            self.label_right_logits.setText(self.logits_right.second_name)

        if file_name == None or file_name == False or file_name == "":
            file_name, _ = QFileDialog.getOpenFileName(self, dir="./data", filter="npy files(*.npy)")
        if file_name == "":
            return
        arr = np.load(file_name).astype(np.float32)
        if arr.ndim == 5 and arr.shape[0] == 1:
            arr = arr[0]
        print(arr.shape, self.image.arr.shape)
        if arr.shape[1:] != self.image.arr.shape:
            print("shape not match")
            arr = np.transpose(arr, (0, 3, 2, 1))
        # arr = arr[:, :, ::-1, ::-1]
        # arr = np.transpose(arr, (0, 3, 2, 1))
        if pos == "left" or self.logits_left is None:
            setup_left_logits(arr, file_name)
        if pos == "right" or self.logits_right is None:
            setup_right_logits(arr, file_name)

        self.set_logits_cls(self.current_cls)
        self.horizontalSlider_logits.setValue(int(self.logits_opacity * 100))

        if not self.logits_init:
            self.comboBox_logits.addItems([str(cls) for cls in range(arr.shape[0])])
            self.comboBox_logits.setEnabled(True)
            self.horizontalSlider_logits.setEnabled(True)
            self.checkBox_logits.setEnabled(True)
            self.checkBox_logits.setChecked(True)
            self.logits_init = True

    def depth_scrollbar_handler(self, index):
        self.index = index
        self.update_property()
        self.update_view()

    def intensity_slider_handler(self, index):
        if self.sender() == self.horizontalSlider_min:
            if index >= self.image.a_max:
                self.horizontalSlider_min.setValue(self.image.a_min)
                return
            self.image.a_min = index
        else:
            if index <= self.image.a_min:
                self.horizontalSlider_max.setValue(self.image.a_max)
                return
            self.image.a_max = index

        self.image.update_arr()
        self.update_view()

    def seg_slider_handler(self, index):
        self.seg.opacity = index / 100
        self.update_view()

    def set_logits_style(self, style):
        self.logits_left.set_style(style)
        self.logits_right.set_style(style)
        self.update_view()

    def logits_slider_handler(self, index):
        self.logits_opacity = index / 100
        self.update_view()

    def logits_slider_threshold_handler(self, value):
        if self.sender() == self.horizontalSlider_logits_left_low:
            if value >= self.logits_left.threshold_high:
                self.horizontalSlider_logits_left_low.setValue(self.logits_left.threshold_low)
                return
            self.logits_left.threshold_low = value
        elif self.sender() == self.horizontalSlider_logits_left_high:
            if value <= self.logits_left.threshold_low:
                self.horizontalSlider_logits_left_high.setValue(self.logits_left.threshold_high)
                return
            self.logits_left.threshold_high = value
        elif self.sender() == self.horizontalSlider_logits_right_low:
            if value >= self.logits_right.threshold_high:
                self.horizontalSlider_logits_right_low.setValue(self.logits_right.threshold_low)
                return
            self.logits_right.threshold_low = value
        elif self.sender() == self.horizontalSlider_logits_right_high:
            if value <= self.logits_right.threshold_low:
                self.horizontalSlider_logits_right_high.setValue(self.logits_right.threshold_high)
                return
            self.logits_right.threshold_high = value

        self.update_view()

    def set_seg_visible(self, state):
        self.seg.visible = self.checkBox_seg.isChecked()
        self.update_view()

    def set_logits_visible(self, state):
        self.logits_left.visible = self.checkBox_logits.isChecked()
        self.logits_right.visible = self.checkBox_logits.isChecked()
        self.update_view()
    
    def last_cls(self):
        if self.current_cls > 0:
            self.comboBox_logits.setCurrentIndex(self.current_cls - 1)
    
    def next_cls(self):
        if self.current_cls < self.num_classes - 1:
            self.comboBox_logits.setCurrentIndex(self.current_cls + 1)

    def set_logits_cls(self, cls):
        self.current_cls = int(cls)
        self.logits_left.set_cls(self.current_cls)
        threshold_range = self.logits_left.get_range()
        self.horizontalSlider_logits_left_low.setRange(*threshold_range)
        self.horizontalSlider_logits_left_high.setRange(*threshold_range)
        self.horizontalSlider_logits_left_low.setValue(threshold_range[0])
        self.horizontalSlider_logits_left_high.setValue(threshold_range[1])
        self.spinBox_logits_left_low_value.setRange(*threshold_range)
        self.spinBox_logits_left_high_value.setRange(*threshold_range)
        self.spinBox_logits_left_low_value.setValue(threshold_range[0])
        self.spinBox_logits_left_high_value.setValue(threshold_range[1])

        self.logits_right.set_cls(self.current_cls)
        threshold_range = self.logits_right.get_range()
        self.horizontalSlider_logits_right_low.setRange(*threshold_range)
        self.horizontalSlider_logits_right_high.setRange(*threshold_range)
        self.horizontalSlider_logits_right_low.setValue(threshold_range[0])
        self.horizontalSlider_logits_right_high.setValue(threshold_range[1])
        self.spinBox_logits_right_low_value.setRange(*threshold_range)
        self.spinBox_logits_right_high_value.setRange(*threshold_range)
        self.spinBox_logits_right_low_value.setValue(threshold_range[0])
        self.spinBox_logits_right_high_value.setValue(threshold_range[1])

        self.update_view()

    def scene_MousePressEvent(self, event):
        if not self.visible:
            return
        if event.buttons() == Qt.MiddleButton or event.buttons() == Qt.LeftButton:
                self.preMousePosition = event.scenePos()

    def scene_mouseMoveEvent(self, event):
        if not self.visible:
            return

        x, y = event.scenePos().x(), event.scenePos().y()
        x0, y0 = self.pixmapItem_left.pos().x(), self.pixmapItem_left.pos().y()
        self.h = int((y - y0) // self.ratio)
        self.w = int((x - x0) // self.ratio)
        if self.h < 0:
            self.h = 0
        if self.w < 0:
            self.w = 0
        if self.h >= self.image.h:
            self.h = self.image.h - 1
        if self.w >= self.image.w:
            self.w = self.image.w - 1
        self.update_property()

        if event.buttons() == Qt.MiddleButton or event.buttons() == Qt.LeftButton:
            self.MouseMove = event.scenePos() - self.preMousePosition
            self.preMousePosition = event.scenePos()
            self.pixmapItem_left.setPos(self.pixmapItem_left.pos() + self.MouseMove)
            self.pixmapItem_right.setPos(self.pixmapItem_right.pos() + self.MouseMove)

    def scene_wheelEvent(self, event):
        if not self.visible:
            return
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier:
            angle = event.delta() / 8  # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
            if angle > 0:
                self.ratio += self.zoom_step  # 缩放比例自加
                if self.ratio > self.zoom_max:
                    self.ratio = self.zoom_max
                else:
                    w = self.pixmap_left.size().width() * (self.ratio - self.zoom_step)
                    h = self.pixmap_left.size().height() * (self.ratio - self.zoom_step)
                    x1 = self.pixmapItem_left.pos().x()  # 图元左位置
                    x2 = self.pixmapItem_left.pos().x() + w  # 图元右位置
                    y1 = self.pixmapItem_left.pos().y()  # 图元上位置
                    y2 = self.pixmapItem_left.pos().y() + h  # 图元下位置
                    if event.scenePos().x() > x1 and event.scenePos().x() < x2 \
                            and event.scenePos().y() > y1 and event.scenePos().y() < y2:  # 判断鼠标悬停位置是否在图元中
                        self.pixmapItem_left.setScale(self.ratio)  # 缩放
                        self.pixmapItem_right.setScale(self.ratio)  # 缩放
                        a1 = event.scenePos() - self.pixmapItem_left.pos()  # 鼠标与图元左上角的差值
                        a2 = self.ratio / (self.ratio - self.zoom_step) - 1  # 对应比例
                        delta = a1 * a2
                        self.pixmapItem_left.setPos(self.pixmapItem_left.pos() - delta)
                        self.pixmapItem_right.setPos(self.pixmapItem_right.pos() - delta)
                        # ----------------------------分维度计算偏移量-----------------------------
                        # delta_x = a1.x()*a2
                        # delta_y = a1.y()*a2
                        # self.pixmapItem_left.setPos(self.pixmapItem_left.pos().x() - delta_x,
                        #                        self.pixmapItem_left.pos().y() - delta_y)  # 图元偏移
                        # -------------------------------------------------------------------------

                    else:
                        self.pixmapItem_left.setScale(self.ratio)  # 缩放
                        self.pixmapItem_right.setScale(self.ratio)  # 缩放
                        delta_x = (self.pixmap_left.size().width() * self.zoom_step) / 2  # 图元偏移量
                        delta_y = (self.pixmap_left.size().height() * self.zoom_step) / 2
                        self.pixmapItem_left.setPos(self.pixmapItem_left.pos().x() - delta_x,
                                                    self.pixmapItem_left.pos().y() - delta_y)  # 图元偏移
                        self.pixmapItem_right.setPos(self.pixmapItem_right.pos().x() - delta_x,
                                               self.pixmapItem_right.pos().y() - delta_y)  # 图元偏移
            else:
                self.ratio -= self.zoom_step
                if self.ratio < 0.2:
                    self.ratio = 0.2
                else:
                    w = self.pixmap_left.size().width() * (self.ratio + self.zoom_step)
                    h = self.pixmap_left.size().height() * (self.ratio + self.zoom_step)
                    x1 = self.pixmapItem_left.pos().x()
                    x2 = self.pixmapItem_left.pos().x() + w
                    y1 = self.pixmapItem_left.pos().y()
                    y2 = self.pixmapItem_left.pos().y() + h
                    if event.scenePos().x() > x1 and event.scenePos().x() < x2 \
                            and event.scenePos().y() > y1 and event.scenePos().y() < y2:
                        self.pixmapItem_left.setScale(self.ratio)  # 缩放
                        self.pixmapItem_right.setScale(self.ratio)  # 缩放
                        a1 = event.scenePos() - self.pixmapItem_left.pos()  # 鼠标与图元左上角的差值
                        a2 = self.ratio / (self.ratio + self.zoom_step) - 1  # 对应比例
                        delta = a1 * a2
                        self.pixmapItem_left.setPos(self.pixmapItem_left.pos() - delta)
                        self.pixmapItem_right.setPos(self.pixmapItem_right.pos() - delta)
                        # ----------------------------分维度计算偏移量-----------------------------
                        # delta_x = a1.x()*a2
                        # delta_y = a1.y()*a2
                        # self.pixmapItem_left.setPos(self.pixmapItem_left.pos().x() - delta_x,
                        #                        self.pixmapItem_left.pos().y() - delta_y)  # 图元偏移
                        # -------------------------------------------------------------------------
                    else:
                        self.pixmapItem_left.setScale(self.ratio)
                        self.pixmapItem_right.setScale(self.ratio)
                        delta_x = (self.pixmap_left.size().width() * self.zoom_step) / 2
                        delta_y = (self.pixmap_left.size().height() * self.zoom_step) / 2
                        self.pixmapItem_left.setPos(self.pixmapItem_left.pos().x() + delta_x, self.pixmapItem_left.pos().y() + delta_y)
                        self.pixmapItem_right.setPos(self.pixmapItem_right.pos().x() + delta_x, self.pixmapItem_right.pos().y() + delta_y)
        else:
            if event.delta() > 0:
                index = self.index + 1
                index = min(index, self.image.d - 1)
                self.viewer.mainScrollBar.setValue(index)
            else:
                index = self.index - 1
                index = max(index, 0)
                self.viewer.mainScrollBar.setValue(index)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key.Key_Down or key == Qt.Key.Key_S:
            index = self.index + 1
            index = min(index, self.image.d - 1)
            self.viewer.mainScrollBar.setValue(index)
        elif key == Qt.Key.Key_Up or key == Qt.Key.Key_W:
            index = self.index - 1
            index = max(index, 0)
            self.viewer.mainScrollBar.setValue(index)
        elif key == Qt.Key.Key_A:
            self.last_cls()
        elif key == Qt.Key.Key_D:
            self.next_cls()


    def dragEnterEvent(self, event: PySide6.QtGui.QDragEnterEvent) -> None:
        event.accept()

    def dropEvent(self, event: PySide6.QtGui.QDropEvent) -> None:
        urls = event.mimeData().urls()
        file_names = [url.toLocalFile() for url in urls]
        self.reader = DataReader(file_names=file_names)
        self.reader.signal.connect(self.dropFileHandler)
        self.reader.show()

    def dropFileHandler(self, pairs: list[tuple]):
        func = {
            "Volume": (self.open_file, 0),
            "Segmentation": (self.open_seg, 1),
            "Logits (left)": (partial(self.open_logits, pos="left"), 2),
            "Logits (right)": (partial(self.open_logits, pos="right"), 3),
        }
        pairs.sort(key=lambda tup: func[tup[1]][1])
        for file_name, type_ in pairs:
            func[type_][0](file_name)

    def showLogitsWindow(self, event):
        self.logitsWindow.show()

    def exit_(self):
        self.viewer.close()
        self.close()

    def viewer_hide(self):
        self.viewer.hide()
    
    def logitsWindow_hide(self):
        self.logitsWindow.hide()

    def show_(self):
        self.viewer.show()

