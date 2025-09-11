from pathlib import Path
from ..data import data_loader
import cv2

def resize_image(img_path):
    img = cv2.imread(img_path)
    resized = cv2.resize(img, (256, 256))
    return resized

def normalize_image(img):
    normalized = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    return normalized

if __name__ == "__main__":
    cwd = Path.cwd()
    data_root = cwd / r"data"
    if not data_root.exists():
        data_root.touch()

    raw_data = data_loader.load_data(data_root, "raw")
    sample_data = raw_data[0]
    resized = resize_image(sample_data)
    normalized = normalize_image(resized)

    cv2.imshow("Image Viewer", normalized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()