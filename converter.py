import cv2
import pytesseract


class Converter:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = (
            "C:/Program Files/Tesseract-OCR/tesseract.exe"
        )

    def convert_img_to_text(self, img_path):
        # Read image from which text needs to be extracted
        img = cv2.imread(img_path)

        # Preprocessing the image starts

        # Convert the image to gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Performing OTSU threshold
        ret, thresh1 = cv2.threshold(
            gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV
        )

        # Specify structure shape and kernel size.
        # Kernel size increases or decreases the area
        # of the rectangle to be detected.
        # A smaller value like (10, 10) will detect
        # each word instead of a sentence.
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

        # Applying dilation on the threshold image
        dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

        # Finding contours
        contours, hierarchy = cv2.findContours(
            dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )

        # Looping through the identified contours
        # Then rectangular part is cropped and passed on
        # to pytesseract for extracting text from it
        # Extracted text is then written into a text file
        with open("recognized.txt", "a", encoding="utf-8") as file:
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)

                # Cropping the text block for giving input to OCR
                cropped = gray[y : y + h, x : x + w]

                # Apply OCR on the cropped image
                text = pytesseract.image_to_string(cropped, lang="tur")

                # Appending the text into file
                file.write(text + "\n")
