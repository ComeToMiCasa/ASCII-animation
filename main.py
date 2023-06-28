import generator
import video
import argparse
import os
from rembg import remove


def video_to_ascii(path_in, path_out, w, f, rem_bg):
    try:
        os.mkdir(f"./ascii/{path_out}")
    except Exception as e:
        pass

    images = video.extract_images_from_video(
        path_in, 500 if f is None else int(1000 / int(f))
    )

    if rem_bg is True:
        for idx, img in enumerate(images):
            images[idx] = remove(img)

    cnt = 0
    for image in images:
        generator.generate_ascii(
            image, f"{path_out}/frame_{cnt}", 100 if w is None else int(w)
        )
        cnt += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_in", help="path to the desired video file")
    parser.add_argument("path_out", help="name of the output folder")
    parser.add_argument(
        "-rb",
        "--remove_background",
        action="count",
        help="[optional] remove background if set",
    )
    parser.add_argument("-w", "--width", help="[optional] width to resize image")
    parser.add_argument(
        "-f", "--freq", help="[optional] no. of frames to capture per second"
    )

    args = parser.parse_args()

    video_to_ascii(
        args.path_in,
        args.path_out,
        args.width,
        args.freq,
        False if args.remove_background is None else True,
    )
