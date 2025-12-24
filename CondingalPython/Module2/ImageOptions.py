import cv2
import matplotlib.pyplot as plt

file = input("Which image do you want to convert?\n")
image = cv2.imread(file)

option = input("Do you want an RGB image, gray_image or both?\n 'RGB' 'gray' 'both'\n").lower()
def rgb():
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title("RGB Image")
    plt.show()
def gray():
    gray_image =  cv2.cvtColor(image, cv2. COLOR_BGR2GRAY)
    plt.imshow(gray_image, cmap='gray')
    plt.title("Grayscale Image")
    plt.show()
if option == 'rgb':
    rgb()
elif option == 'gray':
    gray()
cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()