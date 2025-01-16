# Video https://youtu.be/jMXXsbkHSAs
# Post http://kontakts.ru/showthread.php/40884?p=86146#post86146
import mfrc522
from machine import Pin
import time

# Инициализация пинов для MFRC522
sck = 6
mosi = 7
miso = 4
cs = 5  # SDA pin
rst = 22
button_pin = 12  # Пин для кнопки

# Инициализация кнопки
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

def do_write():
    rdr = mfrc522.MFRC522(sck=sck, mosi=mosi, miso=miso, rst=rst, cs=cs)
    print("")
    print("Place card before reader to read from address 0x08")
    print("")

    try:
        while True:
            # Запрос на чтение карты
            (stat, tag_type) = rdr.request(rdr.REQIDL)
            if stat == rdr.OK:
                # Считывание UID карты
                (stat, raw_uid) = rdr.anticoll()
                if stat == rdr.OK:
                    print("New card detected")
                    print("  - tag type: 0x%02x" % tag_type)
                    print("  - uid : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                    print("")

                    # Выбор карты и авторизация
                    if rdr.select_tag(raw_uid) == rdr.OK:
                        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                        if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                            data = rdr.read(8)  # Чтение данных с 8-го блока
                            print("Data in sector 8: ", data)

                            # Проверка, если все байты равны 0
                            if all(byte == 0 for byte in data):
                                print("Sector 8 is empty.")
                                print("Press the button to write data.")
                                # Ожидание нажатия кнопки
                                while button.value() == 1:  # Ожидание нажатия кнопки
                                    time.sleep(0.1)
                                
                                # Запись данных в 8-й блок
                                print("Writing data to sector 8...")
                                stat = rdr.write(8, b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f")
                                if stat == rdr.OK:
                                    print("Data written to sector 8")
                                else:
                                    print("Failed to write data to sector 8")

                                # После завершения записи
                                print("Remove the card and press the button to continue.")
                                while button.value() == 1:  # Ожидание нажатия кнопки
                                    time.sleep(0.1)
                                print("Returning to start.")
                            else:
                                print("Sector 8 already contains data.")
                                print("Press the button to format the card.")
                                # Ожидание нажатия кнопки для форматирования
                                while button.value() == 1:  # Ожидание нажатия кнопки
                                    time.sleep(0.1)
                                    
                                print("Formatting card...")
                                # Форматирование сектора (очистка данных)
                                stat = rdr.write(8, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
                                if stat == rdr.OK:
                                    print("Card formatted. Data cleared from sector 8.")
                                else:
                                    print("Failed to format the card.")

                                # После завершения форматирования
                                print("Remove the card and press the button to continue.")
                                while button.value() == 1:  # Ожидание нажатия кнопки
                                    time.sleep(0.1)
                                print("Returning to start.")

                            # Очистка и переход к следующему циклу
                            print("Cycle completed, restarting...")
                            time.sleep(2)  # Небольшая задержка перед началом нового цикла
                            return  # Возврат в начало программы, повторный запуск do_write()

                        else:
                            print("Authentication error")
                    else:
                        print("Failed to select tag")

    except KeyboardInterrupt:
        print("Bye")

if __name__ == '__main__':
    while True:
        do_write()  # Запуск процесса записи на карту
