# Video https://youtu.be/C3u8n6HeBkQ
# Post http://kontakts.ru/showthread.php/40884?p=86212#post86212
# Telega https://t.me/MrMicroPython
# Лицензия Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA)
import machine
import gc
import sys
from time import sleep, sleep_ms
import utime
from machine import ADC, Pin

# Получение уникального идентификатора устройства (каждое устройство имеет свой уникальный ID)
unique_id = machine.unique_id()

# Чтение температуры с встроенного датчика на RP2040
# Встроенный датчик температуры подключен к ADC4
sensor_temp = ADC(4)  # Встроенный датчик температуры на ADC4
conversion_factor = 3.3 / (65535)  # Преобразователь, чтобы привести значение ADC к реальному напряжению

# Считывание данных с датчика температуры и расчет реальной температуры
reading = sensor_temp.read_u16() * conversion_factor  # Считывание значения с датчика и преобразование
temperature = 27 - (reading - 0.706) / 0.001721  # Преобразование показаний в температуру (формула для RP2040)

# Получение информации о памяти (сбор мусора)
gc.collect()  # Принудительный запуск сборщика мусора для освобождения памяти
free_memory = gc.mem_free()  # Количество свободной памяти в байтах
allocated_memory = gc.mem_alloc()  # Количество выделенной памяти в байтах

# Получение информации о версии MicroPython и платформе
mp_version = sys.version  # Версия MicroPython
platform = sys.platform  # Платформа (например, 'rp2' для Raspberry Pi Pico)

while True:
    # Пересчитываем время работы в секундах (можно добавить в будущем)

    # Вывод всей системной информации
    print("=============================")
    print("System Info:")  # Заголовок для вывода информации
    print("=============================")
    
    # Уникальный идентификатор устройства
    print("Unique ID:", unique_id)
    
    # Выводим текущую температуру, считанную с датчика
    print("CPU Temperature: %.2f C" % temperature)
    
    # Память: свободная и выделенная
    print("Free memory (bytes):", free_memory)
    print("Allocated memory (bytes):", allocated_memory)
    
    # Информация о версии MicroPython и платформе
    print("MicroPython version:", mp_version)
    print("Platform:", platform)
    
    # Печать пустых строк для улучшения читаемости
    print("  ")
    print("  ")

    # Пауза перед следующим обновлением (интервал в 2 секунды)
    utime.sleep(2)
    sleep(1)  # Небольшая задержка, чтобы предотвратить перегрузку процессора
