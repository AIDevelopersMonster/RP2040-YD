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

# Функция объяснения умножения и нейтрального элемента
def explain_multiplication():
    print("                                        ")
    print(" \U0001F4A1 ОПРЕДЕЛЕНИЕ:                        ")
    print("\u250C" + "\u2500" * 38 + "\u2510")
    print("│ Умножение — это математическая       │")
    print("│ операция, означающая сложение числа  │")
    print("│ самого с собой несколько раз.        │")
    print("│ Например:                            │")
    print("│                                      │")
    print("│  3 × 2 = 3 + 3 = 6                   │")
    print("│                                      │")
    print("│ 🔹 Число 1 — нейтральный элемент.    │")
    print("│ При умножении на него число          │")
    print("│ не изменяется:                       │")
    print("│  7 × 1 = 7                           │")
    print("\u2514" + "\u2500" * 38 + "\u2518\n")
    print("Теперь попробуем умножить два числа!\n")

# Функция генерации примера
def generate_problem():
    a = random.randint(1, 9)  # Генерируем случайные числа
    b = 1  # Нейтральный элемент в умножении
    correct_answer = a * b
    return a, b, correct_answer

# Функция проверки ответа с кнопкой
def check_answer():
    try:
        while True:
            a, b, correct_answer = generate_problem()
            print(f"\nРешите пример: {a} × {b} = ?")

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

            if b == 1:
                print(f"ℹ️ {a} × {b} = {correct_answer}, потому что при умножении на 1 число не изменяется тк 1 нейтральный элемент. ")

            time.sleep(1)  # Даем время посмотреть результат
            show_color((0, 0, 0))  # Выключаем светодиоды
            print("\nСледующий пример...\n")
    
    except KeyboardInterrupt:
        print("\n🚪 Выход из программы. До свидания!")
        show_color((0, 0, 0))  # Выключаем светодиоды перед выходом

# Основная программа
explain_multiplication()  # Объясняем умножение
check_answer()  # Запускаем тесты
