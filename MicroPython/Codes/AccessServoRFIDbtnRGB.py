# Video https://youtu.be/hMVxpWt_qS8
# Post ttp://kontakts.ru/showthread.php/40884?p=86147#post86147
import mfrc522
from machine import Pin
from servo import Servo
import utime

# Инициализация сервопривода и пинов для подключения
s1 = Servo(0)

# Пины для подключения MFRC522
sck = 6
mosi = 7
miso = 4
cs = 5  # SDA pin
rst = 22

# Пины для подключения кнопки и RGB-светодиода
button_pin = Pin(15, Pin.IN, Pin.PULL_UP)  # Пин кнопки (подтянут к VCC)
red_pin = Pin(16, Pin.OUT)  # Красный светодиод
green_pin = Pin(17, Pin.OUT)  # Зеленый светодиод

# Функция для установки угла сервопривода
def servo_Angle(angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s1.goto(round(angle*1024/180))

# Функция для установки состояния светодиодов
def set_led_state(is_open):
    if is_open:
        green_pin.value(1)  # Включаем зеленый
        red_pin.value(0)    # Выключаем красный
    else:
        green_pin.value(0)  # Выключаем зеленый
        red_pin.value(1)    # Включаем красный

# Основная функция чтения данных с карты и управления замком
def do_read():
    rdr = mfrc522.MFRC522(sck=sck, mosi=mosi, miso=miso, rst=rst, cs=cs)
    print("")
    print("Place card before reader to read from address 0x08")
    print("")

    lock_open = False  # Состояние замка (по умолчанию закрыт)

    try:
        while True:
            num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  # Код доступа
            (stat, tag_type) = rdr.request(rdr.REQIDL)  # Ожидаем картку
            if stat == rdr.OK:
                (stat, raw_uid) = rdr.anticoll()  # Считываем UID карты
                if stat == rdr.OK:
                    print("New card detected")
                    print("  - tag type: 0x%02x" % tag_type)
                    print("  - uid : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                    print("")
                    if rdr.select_tag(raw_uid) == rdr.OK:
                        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]  # Ключ для аутентификации
                        if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                            # Читаем данные с 8-го сектора
                            print("Address 8 data: %s" % rdr.read(8))
                            # Если данные карты совпадают с ожидаемыми
                            if rdr.read(8) == num:
                                print("Correct data, unlocking...")
                                # Открытие замка
                                servo_Angle(90)  # Переводим сервопривод в положение для открытия замка
                                set_led_state(True)  # Включаем зеленый светодиод
                                lock_open = True
                            else:
                                print("Incorrect data, locking...")
                                # Закрытие замка
                                servo_Angle(0)  # Переводим сервопривод в положение для закрытия замка
                                set_led_state(False)  # Включаем красный светодиод
                                lock_open = False
                            rdr.stop_crypto1()  # Останавливаем криптографию
                        else:
                            print("Authentication error")
                    else:
                        print("Failed to select tag")

            # Проверка кнопки для закрытия замка
            if not button_pin.value():  # Кнопка нажата (LOW, так как подтянут к VCC)
                if lock_open:  # Если замок открыт, закрываем
                    print("Button pressed, locking...")
                    servo_Angle(0)  # Переводим сервопривод в положение для закрытия замка
                    set_led_state(False)  # Включаем красный светодиод
                    lock_open = False
                else:
                    print("Button pressed, but lock is already closed.")

            utime.sleep(0.1)  # Пауза перед следующей итерацией

    except KeyboardInterrupt:
        print("Bye")

if __name__ == '__main__':
    do_read()  # Чтение данных с карты и управление замком

