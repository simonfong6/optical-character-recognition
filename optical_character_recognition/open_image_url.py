"""
Code from https://www.pyimagesearch.com/2015/03/02/convert-url-to-image-with-python-and-opencv/
"""
from urllib.request import urlopen

import cv2
import numpy as np


# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# return the image
	return image

if __name__ == '__main__':
    # initialize the list of image URLs to download
    urls = [
        "https://pyimagesearch.com/wp-content/uploads/2015/01/opencv_logo.png",
        "https://pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png",
        "https://pyimagesearch.com/wp-content/uploads/2014/12/adrian_face_detection_sidebar.png",
    ]
    # loop over the image URLs
    for url in urls:
        # download the image URL and display it
        print("downloading %s" % (url))
        image = url_to_image(url)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
