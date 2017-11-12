import numpy as np

def y_grayscale(rgb_image):
    """Return a grayscale version of the RGB image, using the Y channel of the YCbCr color space."""
    # For details on the YCbCr color space, see:
    # https://en.wikipedia.org/wiki/YCbCr
    # https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.601-7-201103-I!!PDF-E.pdf
    return (.299 * rgb_image[:, :, 0] +
            .587 * rgb_image[:, :, 1] +
            .114 * rgb_image[:, :, 2]).round().astype(np.uint8)
