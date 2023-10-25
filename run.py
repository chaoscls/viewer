import argparse
from typing import List

from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow


def get_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num_classes', type=int, default=19)
    parser.add_argument('-d', '--dummy_data_size', nargs='+', type=int, default=None)
    return parser.parse_args()

if __name__ == "__main__":
    opt = get_opt()
    app = QApplication([])
    win = MainWindow(opt.num_classes, opt.dummy_data_size)
    win.show()
    app.exec()
