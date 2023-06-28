import cv2
from PIL import Image
import os


def extract_images_from_video(path_in, interval=500):
    # try:
    #     os.mkdir(f"./images/{path_out}")
    # except Exception as e:
    #     pass

    cnt = 0
    vidcap = cv2.VideoCapture(path_in)

    images = []

    while True:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, cnt * interval)
        success, image = vidcap.read()

        if success is False:
            print("[Frame capture complete]")
            break

        # cv2.imwrite(f"images/{path_out}/capture_{cnt}.jpg", image)

        # opencv image to PIL image
        color_converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        images.append(Image.fromarray(color_converted_image))

        cnt = cnt + 1

    return images


if __name__ == "__main__":
    extract_images_from_video("./sample.mp4", "sample")
