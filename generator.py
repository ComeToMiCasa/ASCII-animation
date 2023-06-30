import PIL.Image
import sys
import argparse

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ".", " "]
# ASCII_CHARS = [" ", ",", ":", ";", "+", "*", "?", "%", "$", "#", "@"]


def resize(image, new_width=100):
    width, height = image.size
    new_height = int(new_width * height / width)
    return image.resize((new_width, new_height))


def to_greyscale(image):
    return image.convert("L")


def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str


def open_path(path):
    try:
        original_image = PIL.Image.open(path)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    return original_image


def generate_ascii(original_image, name, size=100):
    image = resize(original_image, size)
    # convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    # Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i : i + img_width] + "\n"
    # save the string to a file
    with open(f"./ascii/{name}.txt", "w") as f:
        f.write(ascii_img)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to the desired image file")
    parser.add_argument("-w", "--width", help="[optional] width to resize image")
    args = parser.parse_args()

    if args.width:
        generate_ascii(open_path(args.path), 0, args.width)
    else:
        generate_ascii(open_path(args.path), 0)
