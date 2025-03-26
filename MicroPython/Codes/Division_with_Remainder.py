from machine import Pin
import neopixel
import time
import random
import sys

# Настройка кнопки (GPIO 24) и светодиодов WS2812 (GPIO 23)
button = Pin(24, Pin.IN, Pin.PULL_UP)
num_leds = 1
np = neopixel.NeoPixel(Pin(23), num_leds)

# Функция для изменения цвета светодиодов
def show_color(color):
    for i in range(num_leds):
        np[i] = color
    np.write()

# Функция объяснения деления с псевдографикой
def explain_division():
    print("                                        ")
    print(" 📢 ОПРЕДЕЛЕНИЕ:                        ")
    print("┌──────────────────────────────────────┐")
    print("│ Деление — это операция, которая     │")
    print("│ определяет, сколько раз одно число  │")
    print("│ содержится в другом. Например:      │")
    print("│                                      │")
    print("│  6 ÷ 2 = 3                          │")
    print("└──────────────────────────────────────┘\n")
    print("Теперь попробуем поделить два числа!\n")

# Функция генерации примера
def generate_problem():
    b = random.randint(1, 9)  # Генерируем случайное делитель (от 1 до 9)
    a = b * random.randint(1, 9)  # Генерируем числитель, который делится на b
    correct_answer = a // b  # Ответ на деление (целочисленное деление)
    return a, b, correct_answer

# Функция пояснения решения задачи
def explain_problem(a, b, correct_answer):
    print(f"Пример {a} ÷ {b}:")
    print(f"Делим число {a} на {b}.")
    print(f"Задача заключается в том, чтобы узнать, сколько раз {b} входит в число {a}.")
    
    # Объяснение через последовательное вычитание
    quotient = 0
    remainder = a
    print(f"Мы будем вычитать {b} из {a} до тех пор, пока это возможно.")
    while remainder >= b:
        remainder -= b
        quotient += 1
    print(f"После {quotient} вычитаний остаток равен {remainder}.")
    print(f"Итак, {a} ÷ {b} = {quotient} с остатком {remainder}.")
    
    if remainder == 0:
        print(f"Ответ: {quotient}, остатка нет.")
    else:
        print(f"Ответ: {quotient} с остатком {remainder}.")

# Функция проверки ответа с кнопкой
def check_answer():
    while True:
        a, b, correct_answer = generate_problem()
        explain_problem(a, b, correct_answer)  # Поясняем решение
        print(f"\nРешите пример: {a} ÷ {b} = ?")
        
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

# Основная программа
explain_division()  # Объясняем деление
check_answer()  # Запускаем тесты

try:
    explain_problem()  # Объясняем деление
    check_answer()  # Запускаем тесты
except KeyboardInterrupt:
    print("\n🚪 Программа завершена пользователем. До встречи!")
    show_color((0, 0, 0))  # Выключаем светодиоды
    sys.exit(0)  # Корректный выход без ошибки