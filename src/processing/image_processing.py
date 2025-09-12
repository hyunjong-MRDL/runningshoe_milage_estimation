import cv2

def resize_image(img_path):
    img = cv2.imread(img_path)
    resized = cv2.resize(img, (256, 256))
    return resized

def normalize_image(img):
    normalized = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    return normalized

if __name__ == "__main__":
    from pathlib import Path

    cwd = Path.cwd()
    data_root = cwd / r"data/raw"
    raw_data = [f for f in data_root.iterdir() if f.is_file()]

    sample = raw_data[0]
    processed = normalize_image(resize_image(sample))

    cv2.imshow("Image Viewer", processed)
    cv2.waitKey()
    cv2.destroyAllWindows()

    processed_root = data_root / r"processed"
    for raw in raw_data:
        processed_name = processed_root / raw.name
        processed_img = normalize_image(resize_image(raw))
        cv2.imwrite(processed_name, processed_img)