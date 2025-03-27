from machine import Pin
import neopixel
import time
import random

# Настройка кнопки (GPIO 24) и светодиода WS2812 (GPIO 23)
button = Pin(24, Pin.IN, Pin.PULL_UP)
num_leds = 1
np = neopixel.NeoPixel(Pin(23), num_leds)

# Функция для изменения цвета светодиода
def show_color(color):
    np[0] = color
    np.write()

# Функция объяснения обратного элемента в умножении
def explain_multiplicative_inverse():
    print("                                        ")
    print(" 📢 ОПРЕДЕЛЕНИЕ:                        ")
    print("┌──────────────────────────────────────┐")
    print("│ Обратный элемент в умножении для     │")
    print("│ числа x — это число, при умножении   │")
    print("│ на которое получается 1. Например:   │")
    print("│                                      │")
    print("│  2 × 0.5 = 1                         │")
    print("│                                      │")
    print("│ 🔹 Обратный элемент не существует    │")
    print("│ для числа 0.                         │")
    print("└──────────────────────────────────────┘\n")
    print("Теперь попробуем найти обратный элемент для различных чисел!\n")

# Функция генерации примера
def generate_problem():
    a = random.randint(1, 9)  # Генерируем случайное число от 1 до 9
    multiplicative_inverse = 1 / a
    correct_answer = 1
    return a, multiplicative_inverse, correct_answer

# Функция проверки ответа с кнопкой
def check_answer():
    try:
        while True:
            a, multiplicative_inverse, correct_answer = generate_problem()
            print(f"\nРешите пример: {a} × ? = 1")
            print("Введите число с плавающей точкой, например, 0.5:")

            try:
                user_answer = float(input("Введите ваш ответ: "))
            except ValueError:
                print("❌ Ошибка: Введите число с плавающей точкой!")
                continue

            print("Нажмите кнопку для проверки ответа...")

            while button.value():  # Ждём нажатия кнопки
                time.sleep(0.1)

            if abs(user_answer - multiplicative_inverse) < 0.01:
                print("✅ Правильно!")
                show_color((0, 255, 0))  # Зеленый цвет
            else:
                print(f"❌ Ошибка! Правильный ответ: {multiplicative_inverse:.2f}")
                show_color((255, 0, 0))  # Красный цвет

            print(f"ℹ️ {a} × {multiplicative_inverse:.2f} = 1, потому что {multiplicative_inverse:.2f} — это обратный элемент для {a}.")

            time.sleep(1)  # Даем время посмотреть результат
            show_color((0, 0, 0))  # Выключаем светодиод
            print("\nСледующий пример...\n")
    
    except KeyboardInterrupt:
        print("\n🚪 Выход из программы. До свидания!")
        show_color((0, 0, 0))  # Выключаем светодиод перед выходом

# Основная программа
explain_multiplicative_inverse()  # Объясняем обратный элемент в умножении
check_answer()  # Запускаем тесты
