from PIL import Image, ImageGrab
import time

# делаем задержку в 2 секунды на выбор
# окна, для которого нужно сделать скриншот
time.sleep(2)

# создание скриншота
img = ImageGrab.grab()
# сохраним скриншот
img.save("test3.jpg", quality="web_medium")
# откроем созданный скриншот
with Image.open("test3.jpg") as img:
    # смотрим, какую информацию
    # пишет библиотека Pillow
    # при создании скриншота
    print(img.info)
img.save("image_name.jpg", quality="web_high")

