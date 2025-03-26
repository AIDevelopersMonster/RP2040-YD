from machine import Pin
import neopixel
import time
import random

# Настройка кнопки (GPIO 24) и светодиодов WS2812 (GPIO 23)
button = Pin(24, Pin.IN, Pin.PULL_UP)
num_leds = 1
np = neopixel.NeoPixel(Pin(23), num_leds)

# Функция для изменения цвета светодиодов
def show_color(color):
    for i in range(num_leds):
        np[i] = color
    np.write()

# Функция для плавного выключения светодиода перед выходом
def fade_out():
    for i in range(255, -1, -5):  # Плавное затухание
        np[0] = (i, 0, 0)
        np.write()
        time.sleep(0.02)
    np[0] = (0, 0, 0)
    np.write()

# Функция объяснения сложения с псевдографикой
def explain_addition():
    print("                                        ")
    print(" 📢 ОПРЕДЕЛЕНИЕ:                        ")
    print("┌──────────────────────────────────────┐")
    print("│ Сложение — это математическая        │")
    print("│ операция, объединяющая два числа     │")
    print("│ и дающая их сумму. Например:         │")
    print("│                                      │")
    print("│  2 + 3 = 5                           │")
    print("└──────────────────────────────────────┘\n")
    print("Теперь попробуем сложить два числа!\n")

# Функция генерации примера
def generate_problem():
    a = random.randint(1, 9)  # Генерируем случайные числа от 1 до 9
    b = random.randint(1, 9)
    correct_answer = a + b
    return a, b, correct_answer

# Функция проверки ответа с кнопкой
def check_answer():
    try:
        while True:
            a, b, correct_answer = generate_problem()
            print(f"\nРешите пример: {a} + {b} = ?")
            
            try:
                user_answer = int(input("Введите ваш ответ: "))
            except ValueError:
                print("❌ Ошибка: Введите число!")
                continue

            print("Нажмите кнопку для проверки ответа...")
            
            while button.value():  # Ждём нажатия кнопки
                time.sleep(0.1)
            
            if user_answer == correct_answer:
                print("✅ Правильно!")
                show_color((0, 255, 0))  # Зеленый цвет
            else:
                print(f"❌ Ошибка! Правильный ответ: {correct_answer}")
                show_color((255, 0, 0))  # Красный цвет
            
            time.sleep(1)  # Даем время посмотреть результат
            show_color((0, 0, 0))  # Выключаем светодиоды
            print("\nСледующий пример...\n")

    except KeyboardInterrupt:
        print("\n🚀 Завершение программы...")
        fade_out()
        print("👋 До встречи!\n")

# Основная программа
explain_addition()  # Объясняем сложение
check_answer()  # Запускаем тесты
