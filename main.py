import cv2
import sys
import pytesseract
import re

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python main.py image.jpg')
        print(cv2.getVersionString())
        print(pytesseract.get_tesseract_version())
        sys.exit(1)

    imPath = sys.argv[1]
    config = '-l eng --oem 1 --psm 3'
    img = cv2.imread(imPath, cv2.IMREAD_GRAYSCALE)

    text = pytesseract.image_to_string(img, config=config)
    # print(type(text))
    text_new = text.split('\n')
    # print(text_new)
    regex = '^Photo Code:'
    for t in text_new:
        if re.match(regex, t) is not None:
            print(t.replace('Photo Code: ', ''))







