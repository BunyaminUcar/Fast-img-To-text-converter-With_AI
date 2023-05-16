import cv2
import pytesseract


class Converter:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = (
            "C:/Program Files/Tesseract-OCR/tesseract.exe"
        )

    def convert_img_to_text(self, img_path):
        # Metnin çıkarılması gereken görüntüyü okuyun
        img = cv2.imread(img_path)

        # Görüntünün ön işlemesine başla

        # Görüntüyü gri tonlamaya dönüştürün
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, thresh1 = cv2.threshold(
            gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV
        )

        # Yapı şeklini ve çekirdek boyutunu belirtin.
        # Çekirdek boyutu alanı artırır veya azaltır
        # algılanacak dikdörtgenin sayısı.
        # (10, 10) gibi daha küçük bir değer algılar
        # bir cümle yerine her kelime.
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

        # Eşik görüntüsüne dilatasyon uygulama
        dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

        # Kontur bulma
        contours, hierarchy = cv2.findContours(
            dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )

        # Belirlenen konturlar arasında döngü
        # Daha sonra dikdörtgen kısım kırpılır ve geçilir
        # ondan metin çıkarmak için pytesseract'a
        # Ayıklanan metin daha sonra bir metin dosyasına yazılır
        with open("recognized.txt", "w", encoding="utf-8") as file:
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)

                # OCR'a girdi vermek için metin bloğunun kırpılması
                cropped = gray[y : y + h, x : x + w]

                # Kırpılan görüntüye OCR uygulayın
                text = pytesseract.image_to_string(cropped, lang="tur")

                # Metni dosyaya ekleme
                file.write(text + "\n")
