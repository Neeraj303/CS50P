import sys
from PIL import Image, ImageOps

def main():
    check_argument()
    shirt = Image.open("shirt.png")
    size = shirt.size
    image = Image.open(sys.argv[1])
    image = ImageOps.fit(image, size)
    image.paste(shirt, shirt)
    image.save(f"{sys.argv[2]}")


def check_argument():

    if len(sys.argv) == 3:
        check_image(sys.argv[1:3])
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def check_image(image_list):

    if not image_list[0].lower().endswith((".png", ".jpg", ".jpeg")):
        sys.exit("Invalid input")
    elif not image_list[1].lower().endswith((".png", ".jpg", ".jpeg")):
        sys.exit("Invalid output")
    elif not ((image_list[0]).split(".")[1] == (image_list[1]).split(".")[1]):
        sys.exit("Input and output have different extension")




if __name__ == "__main__":
    main()
