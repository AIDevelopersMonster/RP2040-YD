from machine import Pin
import neopixel
import time
import random

# Настройка кнопки (GPIO 24) и светодиода WS2812 (GPIO 23)
button = Pin(24, Pin.IN, Pin.PULL_UP)
np = neopixel.NeoPixel(Pin(23), 1)

# Функция для изменения цвета светодиода
def show_color(color):
    np[0] = color
    np.write()

# Функция объяснения обратного элемента в сложении
def explain_inverse_element():
    print("                                        ")
    print(" \U0001F4A1 ОПРЕДЕЛЕНИЕ:                        ")
    print("\u250C" + "\u2500" * 38 + "\u2510")
    print("│ Обратный элемент в сложении — это    │")
    print("│ число, которое при сложении с данным │")
    print("│ даёт ноль. Например:                 │")
    print("│                                      │")
    print("│  5 + (-5) = 0                        │")
    print("\u2514" + "\u2500" * 38 + "\u2518\n")
    print("Теперь попробуем найти сумму двух чисел!\n")

# Функция генерации примера
def generate_problem():
    a = random.randint(-9, 9)
    b = -a  # Обратный элемент
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

            while button.value():
                time.sleep(0.1)

            if user_answer == correct_answer:
                print("✅ Правильно!")
                show_color((0, 255, 0))  # Зеленый цвет
            else:
                print(f"❌ Ошибка! Правильный ответ: {correct_answer}")
                show_color((255, 0, 0))  # Красный цвет

            print(f"ℹ️ {a} + {b} = {correct_answer}, потому что при сложении числа с его обратным элементом получается ноль.")

            time.sleep(1)
            show_color((0, 0, 0))  # Выключаем светодиод
            print("\nСледующий пример...\n")

    except KeyboardInterrupt:
        print("\n🚪 Выход из программы. До свидания!")
        show_color((0, 0, 0))  # Выключаем светодиод перед выходом

# Основная программа
explain_inverse_element()  # Объясняем обратный элемент в сложении
check_answer()  # Запускаем тесты
0
