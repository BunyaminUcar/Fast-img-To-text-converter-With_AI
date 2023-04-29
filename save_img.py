from PIL import ImageGrab
from PIL import Image


img = ImageGrab.grabclipboard()


if isinstance(img, Image.Image):
    img.save("screenshot.png")
