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

# Функция объяснения умножения с псевдографикой
def explain_multiplication():
    print("                                        ")
    print(" 📢 ОПРЕДЕЛЕНИЕ:                        ")
    print("╔══════════════════════════════════════╗")
    print("║ Умножение — это операция,            ║")
    print("║ которая показывает, сколько раз     ║")
    print("║ одно число складывается с другим.   ║")
    print("║ Например: 3 * 4 — это значит, что   ║")
    print("║ число 3 складывается 4 раза:        ║")
    print("║  3 + 3 + 3 + 3 = 12                ║")
    print("╚══════════════════════════════════════╝\n")
    print("Теперь попробуем умножить два числа!\n")

# Функция генерации примера
def generate_problem():
    a = random.randint(1, 9)  # Генерируем случайные числа от 1 до 9
    b = random.randint(1, 9)
    correct_answer = a * b
    return a, b, correct_answer

# Функция проверки ответа с кнопкой
def check_answer():
    while True:
        a, b, correct_answer = generate_problem()
        print(f"\nРешите пример: {a} * {b} = ?")
        
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
            print(f"Правильный ответ: {a} * {b} = {correct_answer}")
            print(f"Объяснение: Умножение — это когда {a} складывается {b} раз, т.е. {a} + {a} + {a} + ... ({b} раз) = {correct_answer}")
        else:
            print(f"❌ Ошибка! Правильный ответ: {correct_answer}")
            show_color((255, 0, 0))  # Красный цвет
            print(f"Объяснение: Умножение — это когда {a} складывается {b} раз, т.е. {a} + {a} + {a} + ... ({b} раз) = {correct_answer}")
        
        time.sleep(1)  # Даем время посмотреть результат
        show_color((0, 0, 0))  # Выключаем светодиоды
        print("\nСледующий пример...\n")

# Основная программа
try:
    explain_multiplication()  # Объясняем умножение
    check_answer()  # Запускаем тесты
except KeyboardInterrupt:
    print("\nПрограмма завершена пользователем (Ctrl + C).")
    show_color((0, 0, 0))  # Выключаем светодиод
