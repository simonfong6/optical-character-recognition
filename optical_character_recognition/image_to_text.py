"""
Half Code from: https://stackabuse.com/pytesseract-simple-python-optical-character-recognition/
Text on Image Code: https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
"""
import cv2
import pytesseract

from open_image_url import url_to_image
from colors import ColorPrint


def load_image_from_path(path):

    image = cv2.imread(args.path)

    return image


def ocr_core(image):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(image)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


def put_text(
        image,
        text,
        org=(17, 50),
        font=cv2.FONT_HERSHEY_SIMPLEX,
        font_scale=0.5,
        color=(255, 0, 0),
        thickness=2,
        line_type=cv2.LINE_AA):

    image = cv2.putText(
            image, text, org, font, font_scale, color, thickness,line_type) 
    
    return image


def main(args):
    
    # Read image.
    if args.path:
        # Read image by path.
        image = load_image_from_path(args.path)
    elif args.url:
        # Read image by url.
        image = url_to_image(args.url)
    else:
        raise ValueError("No image to load.")

    text = ocr_core(image)

    msg = f"Text Read: '{text}'"
    ColorPrint.print_info(msg)
        
    # org 
    org = (17, 50) 
    
    # Using cv2.putText() method 
    image = put_text(image, text, org=org) 

    # Window name in which image is displayed 
    window_name = msg
    
    # Displaying the image
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-p', '--path',
                        help="Path of image to perform OCR.",
                        type=str)

    group.add_argument('-u', '--url',
                        help="Url of image to perform OCR.",
                        type=str,
                        default=None)

    args = parser.parse_args()
    main(args)
