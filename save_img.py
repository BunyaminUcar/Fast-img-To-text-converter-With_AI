import keyboard
from PIL import ImageGrab
from datetime import datetime
import time
import win32clipboard


# shift+win+s kombinasyonu için callback fonksiyonu
def take_screenshot():
    time.sleep(2)
    # Ekran görüntüsünü al
    img = ImageGrab.grabclipboard()
    # Ekran görüntüsü alınmışsa kaydet
    if img:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{now}.png"
        img.save(filename)
        print(f"Screenshot saved as {filename}")
        # Windows panosunu boşalt
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()


# shift+win+s kombinasyonu için hotkey tanımla
keyboard.add_hotkey("shift+win+s", take_screenshot)

# Sonsuz döngü ile programın çalışmasını sürekli hale getir
while True:
    pass
