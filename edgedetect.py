import PIL.Image
import cv2

ASCII_STR = "# "
# ASCII_CHARS = ["█", "▓", "▒", "░", " "]
# ASCII_STR = "Ñ@#W$9876543210?!abc;:+=-,._ "
# ASCII_STR = "@#O%+=|i-:.  "
ASCII_CHARS = [char for char in ASCII_STR]
ASCII_CHARS.reverse()

def move (y, x):
    print("\033[%d;%dH" % (y, x))


def resize_image(image, new_width=200):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join(ASCII_CHARS[int(pixel / (255/(len(ASCII_CHARS)-1)))] for pixel in pixels)
    return characters

def main(new_width=200):
    vid = cv2.VideoCapture(0)

    while(True):
        ret, frame = vid.read()
        if not ret:
            print("Cannot take the frame from webcam")
            break

        smolla = cv2.resize(frame, (200, (100 * frame.shape[0]) // frame.shape[1]))
        img_gray = cv2.cvtColor(smolla, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
        edges1 = cv2.Canny(image=img_blur, threshold1=25, threshold2=30) # Canny Edge Detection

        try:
            image = PIL.Image.fromarray(edges1)
        except:
            print("frame is not a valid array")
            vid.release()
            return


        new_image_data = pixels_to_ascii(grayify(resize_image(image)))

        pixel_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
        
        move(0, 0)
        print(ascii_image)

        
    #     cv2.imshow('frame', frame)

    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break

    vid.release()

main()
