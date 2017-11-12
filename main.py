import cv2 as cv
from unsharpmask import unsharp_mask
from ygrayscale import y_grayscale

def main():
    color_image = cv.imread('images/lalandiz.jpg')
    sharpened_color_image = unsharp_mask(color_image)
    more_sharpened_color_image = unsharp_mask(color_image, amount=2)
    grayscale_image = y_grayscale(color_image)
    sharpened_grayscale_image = unsharp_mask(grayscale_image)
    more_sharpened_grayscale_image = unsharp_mask(grayscale_image, amount=2)
    cv.imwrite('images/lalandiz.sharpened.jpg', sharpened_color_image)
    cv.imwrite('images/lalandiz.sharpened.more.jpg', more_sharpened_color_image)
    cv.imwrite('images/lalandiz.grayscale.jpg', grayscale_image)
    cv.imwrite('images/lalandiz.grayscale.sharpened.jpg', sharpened_grayscale_image)
    cv.imwrite('images/lalandiz.grayscale.sharpened.more.jpg', more_sharpened_grayscale_image)

if __name__ == '__main__':
    main()
