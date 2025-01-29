import machine 
import time

# Создаем список всех пинов GPIO от 0 до 28, исключая 3, 5, 6, 9, 10, 11 (не все могут быть использованы для вывода)
# gpio_pins = [i for i in range(29) if i not in [23, 24, 25]]
gpio_pins = [0, 1, 2, 4, 5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 26, 27, 28] 
# Создаем пины как выходы
pins = [machine.Pin(pin, machine.Pin.OUT) for pin in gpio_pins]

while True:
    for pin in pins:
        pin.on()  # Включаем светодиод
        time.sleep(0.2)  # Ждем 100 миллисекунд
        pin.off()  # Выключаем светодиод
