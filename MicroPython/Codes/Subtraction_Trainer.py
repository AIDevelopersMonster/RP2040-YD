from machine import Pin
import neopixel
import time
import random

# Настройка кнопки (GPIO 24) и светодиодов WS2812 (GPIO 23)
button = Pin(24, Pin.IN, Pin.PULL_UP)
num_leds = 1
np = neopixel.NeoPixel(Pin(23), num_leds)

# Функция для плавного выключения светодиода перед выходом
def fade_out():
    for i in range(255, -1, -5):  # Плавное затухание
        np[0] = (i, 0, 0)
        np.write()
        time.sleep(0.02)
    np[0] = (0, 0, 0)
    np.write()

# Функция для изменения цвета светодиодов
def show_color(color):
   
    np[0] = color
    np.write()

# Функция объяснения вычитания с псевдографикой
def explain_subtraction():
    print("                                        ")
    print(" 📢 ОПРЕДЕЛЕНИЕ:                        ")
    print("┌────────────────────────────────────────┐")
    print("│ Вычитание — это математическая         │")
    print("│ операция, в которой из одного числа    │")
    print("│ вычитается другое. Результат называется│")
    print("│ разностью. Например:                   │")
    print("│                                        │")
    print("│  7 - 3 = 4                             │")
    print("└────────────────────────────────────────┘\n")
    print("Теперь попробуем вычесть два числа!\n")

# Функция генерации примера
def generate_problem():
    a = random.randint(5, 9)  # Генерируем случайные числа от 5 до 9
    b = random.randint(1, a)  # Убедимся, что b не больше a
    correct_answer = a - b
    return a, b, correct_answer

# Функция проверки ответа с кнопкой
def check_answer():
    while True:
        a, b, correct_answer = generate_problem()
        print(f"\nРешите пример: {a} - {b} = ?")
        
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
try:
    explain_subtraction()  # Объясняем вычитание
    check_answer()  # Запускаем тесты
except KeyboardInterrupt:
        print("\n\n🚀 Завершение программы...")
        fade_out()
        print("👋 До встречи!\n")
