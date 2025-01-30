# Video https://youtu.be/TgXlUb0fcmA
# Post http://kontakts.ru/showthread.php/40884?p=86201#post86201
# Telega https://t.me/MrMicroPython
import board  # Импорт модуля для работы с пинами микроконтроллера
import digitalio  # Импорт модуля для управления цифровыми входами и выходами

# Настройка кнопки, подключенной к GPIO26
button = digitalio.DigitalInOut(board.GP26)  # Создаем объект кнопки, привязанный к пину GP26
button.direction = digitalio.Direction.INPUT  # Устанавливаем пин как вход (INPUT)
button.pull = digitalio.Pull.UP  # Включаем внутренний подтягивающий резистор (Pull.UP)

# Переменная для хранения предыдущего состояния кнопки
last_value = button.value  # Сохраняем начальное состояние кнопки

# Бесконечный цикл для отслеживания изменений состояния кнопки
while True:
    if last_value != button.value:  # Проверяем, изменилось ли состояние кнопки
        last_value = button.value  # Обновляем предыдущее состояние кнопки
        if button.value:  # Если значение True (кнопка отпущена)
            print("Button is released")  # Выводим сообщение "Кнопка отпущена"
        else:  # Если значение False (кнопка нажата)
            print("Button is pressed")  # Выводим сообщение "Кнопка нажата"
