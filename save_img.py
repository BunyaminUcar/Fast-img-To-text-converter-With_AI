import os
import keyboard
from PIL import ImageGrab
from datetime import datetime
import time
from converter import Converter

convert = Converter()


# shift+win+s kombinasyonu için callback fonksiyonu
def take_screenshot():
    time.sleep(3)
    # Ekran görüntüsünü al
    img = ImageGrab.grabclipboard()
    # Ekran görüntüsü alınmışsa kaydet
    if img:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{now}.png"
        foldername = "screenshots"
        filepath = os.path.join(foldername, filename)
        img.save(filepath)
        print(f"Screenshot saved as {filepath}")
        # Windows panosunu boşalt

        convert.convert_img_to_text(
            f"C:/Users/UCAR/Desktop/Fast-img-To-text-converter-With_AI/screenshots/{filename}"
        )


# shift+win+s kombinasyonu için hotkey tanımla
keyboard.add_hotkey("shift+win+s", take_screenshot)

# Sonsuz döngü ile programın çalışmasını sürekli hale getir
while True:
    pass
