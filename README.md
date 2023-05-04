# Fast-img-To-text-converter-With_AI
-The aim of this project is to provide a fast conversion from image to text using Windows shortcuts.
To do this, run the program and select an image from a specific region using the win+s+shift shortcut.
You will then find the results in a file named result.txt.
- If you use this repository, 
### 1.Tesseract-OCR
Tesseract OCR is open source software used for text recognition (OCR) operations. You can follow the steps below to install Tesseract OCR:

1. First, go to Tesseract OCR's official website: https://github.com/tesseract-ocr/tesseract
2.To install Tesseract OCR, download the appropriate version for your operating system. Different options may be available, such as a setup file for Windows or a package file for Linux.
3. If you have downloaded the setup file for Windows, double-click it to install it and follow the instructions. If you downloaded a package file for Linux, for example, you can install it using the command "sudo apt-get install tesseract-ocr" for Ubuntu.
4. Run the "tesseract" command in the command prompt to verify that the Tesseract OCR is installed correctly. This should show the current version of Tesseract OCR and instructions for use.
5. You are ready to use Tesseract OCR.

Note:After installing Tesseract OCR you need to change the default location in the __init__ method in the converter.py file
