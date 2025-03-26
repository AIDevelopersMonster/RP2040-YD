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

# Функция объяснения сложения и нейтрального элемента
def explain_addition():
    print("                                        ")
    print(" 📢 ОПРЕДЕЛЕНИЕ:                        ")
    print("┌──────────────────────────────────────┐")
    print("│ Сложение — это математическая        │")
    print("│ операция, объединяющая два числа     │")
    print("│ и дающая их сумму. Например:         │")
    print("│                                      │")
    print("│  2 + 3 = 5                           │")
    print("│                                      │")
    print("│ 🔹 Число 0 — нейтральный элемент.    │")
    print("│ При сложении с ним число не меняется:│")
    print("│  7 + 0 = 7                           │")
    print("└──────────────────────────────────────┘\n")
    print("Теперь попробуем сложить два числа!\n")

# Функция генерации примера
def generate_problem():
    a = random.randint(0, 9)  # Генерируем случайные числа, включая 0
    b = 0
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

            if a == 0 or b == 0:
                print(f"ℹ️ {a} + {b} = {correct_answer}, потому что при сложении с 0 число не меняется.")

            time.sleep(1)  # Даем время посмотреть результат
            show_color((0, 0, 0))  # Выключаем светодиоды
            print("\nСледующий пример...\n")

    except KeyboardInterrupt:
        print("\n🚪 Выход из программы. До свидания!")
        show_color((0, 0, 0))  # Выключаем светодиоды перед выходом

# Основная программа
explain_addition()  # Объясняем сложение
check_answer()  # Запускаем тесты
