from PySide6.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QVBoxLayout, \
    QHBoxLayout, QLabel, QComboBox, QSpacerItem, QSizePolicy, QDialogButtonBox, QDialog
from PySide6.QtCore import Qt, Signal, QSize

class DataReader(QWidget):

    signal = Signal(list)

    def __init__(self, file_names):
        super(DataReader, self).__init__()

        self.setWindowTitle("Add data to the scene")
        self.file_names = file_names

        self.layout = QVBoxLayout()
        num_files = len(file_names)
        self.comboboxs = []
        for name in file_names:
            layout = QHBoxLayout()
            label = QLabel("    "+name)
            label.setStyleSheet(u"background-color:rgb(64,64,64)")
            label.setMinimumSize(QSize(600, 30))
            label.setMaximumSize(QSize(800, 30))
            layout.addWidget(label)
            combobox = QComboBox()
            combobox.addItems(["Volume", "Segmentation", "Logits (left)", "Logits (right)"])
            self.comboboxs.append(combobox)
            layout.addWidget(combobox)
            layout.setStretch(0, 1)
            layout.setStretch(1, 0)
            self.layout.addLayout(layout)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.cancel_button = QPushButton("Cancel")
        self.confirm_button = QPushButton("Confirm")
        self.bottom_layout.addWidget(self.cancel_button)
        self.bottom_layout.addWidget(self.confirm_button)
        self.layout.addLayout(self.bottom_layout)

        self.confirm_button.clicked.connect(self.confirm_button_handler)
        self.cancel_button.clicked.connect(self.cancel_button_handler)

        self.setLayout(self.layout)

    def confirm_button_handler(self):
        types = [(file_name, box.currentText()) for file_name, box in zip(self.file_names, self.comboboxs)]
        self.signal.emit(types)
        self.close()

    def cancel_button_handler(self):
        self.close()



if __name__ == '__main__':
    app = QApplication([])
    win = DataReader(['/Users/chaos/Downloads/artery/unet_spacing/train_1/0_000/0_000_pred1.nii.gz', '/Users/chaos/Downloads/artery/unet_spacing/train_1/0_004/0_004_unet_pred1.nii.gz'])
    win.show()
    app.exec()

