import PIL.Image

ASCII_STR_DARK = " .,:;->+=ixXOWM#B@@"
# ASCII_CHARS = ["@", "B", "X", "O", "l","i", "+", "=", ":", ",", ".", " "]
ASCII_CHARS = [char for char in ASCII_STR_DARK]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height//2))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join(ASCII_CHARS[int(pixel / (255/(len(ASCII_CHARS)-1)))] for pixel in pixels)
    return characters

def main(new_width=100):
    path = "gradient.png"
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid pathname to an image.")
        return


    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)


main()