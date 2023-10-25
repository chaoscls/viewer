import SimpleITK as sitk
import numpy as np
import cv2
from monai.transforms import ScaleIntensityRange
import matplotlib.pyplot as plt

PALETTE = [[0, 0, 0], [180, 120, 120], [6, 230, 230], [80, 50, 50],
           [4, 200, 3], [120, 120, 80], [204, 5, 255],
           [4, 250, 7], [224, 5, 255], [235, 255, 7],
           [150, 5, 61], [120, 120, 70], [8, 255, 51], [255, 6, 82],
           [143, 255, 140], [204, 255, 4], [255, 51, 7], [204, 70, 3],
           [0, 102, 200], [61, 230, 250], [255, 6, 51], [11, 102, 255],
           [255, 7, 71], [255, 9, 224], [9, 7, 230],
           [255, 9, 92], [112, 9, 255], [8, 255, 214], [7, 255, 224],
           [255, 184, 6], [10, 255, 71], [255, 41, 10], [7, 255, 255],
           [224, 255, 8], [102, 8, 255], [255, 61, 6], [255, 194, 7],
           [255, 122, 8], [0, 255, 20], [255, 8, 41], [255, 5, 153],
           [6, 51, 255], [235, 12, 255], [160, 150, 20], [0, 163, 255],
           [140, 140, 140], [250, 10, 15], [20, 255, 0], [31, 255, 0],
           [255, 31, 0], [255, 224, 0], [153, 255, 0], [0, 0, 255],
           [255, 71, 0], [0, 235, 255], [0, 173, 255], [31, 0, 255]]

def get_array_from_file(file_path):
    image = sitk.ReadImage(file_path)
    arr = sitk.GetArrayFromImage(image).astype(np.int32)
    return arr

def normalize(data, a_min, a_max):
    transform = ScaleIntensityRange(a_min=a_min, a_max=a_max, b_min=0, b_max=1, clip=True)
    return transform(data).numpy()

def label2rgb(arr, num_classes):
    d, h, w = arr.shape
    rgb_arr = np.zeros([d, h, w, 3], dtype=np.uint8)
    for cls in range(num_classes+1):
        rgb_arr[arr==cls] = PALETTE[cls]
    return rgb_arr

def get_heatmap(mask: np.ndarray, use_rgb: bool = True, colormap: int = cv2.COLORMAP_JET) -> np.ndarray:
    # cv2.COLORMAP_
    heatmap = cv2.applyColorMap(np.uint8(255 * mask), colormap)
    if use_rgb:
        heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)
    return heatmap

def logits2rgb(arr, colormap="JET"):
    if colormap == "NONE":
        arr = arr.copy().astype(np.int16)
        palette = PALETTE[1:] * 4
        res = np.zeros(list(arr.shape)+[3], dtype=np.uint8)
        for i in range(arr.min(), arr.max() + 1):
            res[arr == i] = palette[i]
        return res

    transform = ScaleIntensityRange(a_min=arr.min(), a_max=arr.max(), b_min=0, b_max=1, clip=True)
    arr = transform(arr)
    res = [get_heatmap(im) for im in arr]
    return np.array(res)

def softmax(arr, axis):
    import torch
    return torch.softmax(torch.tensor(arr), 0).numpy()
    exp = np.exp(arr)
    res = exp / arr.max(axis=axis, keepdims=True)
    return res

if __name__ == '__main__':
    # seg = sitk.ReadImage("/Users/chaos/Downloads/artery/unet_spacing/train_1/0_000/0_000_pred1.nii.gz")
    # seg = sitk.ReadImage("/Users/chaos/Downloads/small_unet_192/val1/img0035/img0035_pred.nii.gz")
    # seg = sitk.ReadImage("/Users/chaos/Downloads/small_unet_192/val1/img0035/img0035_pred.nii.gz")
    # seg = sitk.GetArrayFromImage(seg)
    data = np.load("/Users/chaos/data/ct/test/0_017.npy")
    print(data.shape, data.dtype)
    softmax_data = softmax(data, 0)
    # exit()
    seg = softmax_data[1]
    rgb = logits2rgb(seg)
    rgb[seg == 0] = 0
    for i, im in enumerate(rgb):
        if (im == 0).all():
            continue

        plt.figure(figsize=(10, 10))
        plt.imshow(im)
        plt.title(f"{i}/{rgb.shape[0]}")
        plt.axis("off")
        plt.show()

    # for color in PALETTE:
    #     img = np.zeros([64, 64, 3], dtype=np.uint8)
    #     img[:] = np.array(color)
    #     print(color)
    #     plt.imshow(img)
    #     plt.show()


