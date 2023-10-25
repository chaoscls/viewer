import os

import numpy as np

from utils.tools import *


class Item:

    def __init__(self, arr, file_path):
        self._arr = arr
        self.file_path = file_path
        self.name = os.path.basename(file_path)
        self.second_name = "/".join(file_path.split("/")[-2:])
        self.arr = arr.copy()
        self.opacity: float = 0.1
        self.max = arr.max()
        self.min = arr.min()
        self.visible = True


class ImageItem(Item):

    def __init__(self, arr, file_path):
        super(ImageItem, self).__init__(arr, file_path)
        self.d, self.h, self.w = arr.shape
        self.a_min: int = -1200
        self.a_max: int = 400
        self.update_arr()

    def update_arr(self):
        arr = normalize(self._arr, self.a_min, self.a_max)
        self.arr = np.uint8(arr * 255)


class SegmentationItem(Item):

    def __init__(self, arr, file_path):
        super(SegmentationItem, self).__init__(arr, file_path)
        self.num_classes = arr.max()
        self.rgb = label2rgb(arr, self.num_classes)


class LogitsItem(Item):

    def __init__(self, arr, file_path):
        super(LogitsItem, self).__init__(arr, file_path)
        self.opacity = 0.5
        self.threshold_low: int = -100
        self.threshold_high: int = 100
        self.num_class: int = arr.shape[0]
        self.arr_softmax = np.exp(self.arr)
        self.dict = {cls: logits for cls, logits in enumerate(arr)}
        # self.mask = np.ones(arr[0].shape, dtype=bool)
        self.rgb_dict = {}
        for cls, logits in self.dict.items():
            self.rgb_dict[cls] = logits2rgb(logits)
            # self.mask = self.mask & (logits != 0)
        self.current_cls: int
        self.rgb: np.ndarray
        self.set_cls(0)
    
    def set_cls(self, cls):
        self.current_cls = cls
        self.arr = self.dict[cls]
        self.rgb = self.rgb_dict[cls]

    def get_range(self):
        return (int(self.arr.min()) - 1, int(self.arr.max()) + 1)

    def set_style(self, colormap):
        for cls, logits in self.dict.items():
            self.rgb_dict[cls] = logits2rgb(logits, colormap)
        self.rgb = self.rgb_dict[self.current_cls]
