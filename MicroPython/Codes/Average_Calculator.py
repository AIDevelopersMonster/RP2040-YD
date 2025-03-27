from machine import Pin
import time
import neopixel

# Настройка кнопки (GPIO 24) и светодиодов WS2812 (GPIO 23)
button = Pin(24, Pin.IN, Pin.PULL_UP)
num_leds = 1
np = neopixel.NeoPixel(Pin(23), num_leds)

# Функция для изменения цвета светодиодов
def show_color(color):
    for i in range(num_leds):
        np[i] = color
    np.write()

# Функция объяснения среднего значения
def explain_average():
    print("ОПРЕДЕЛЕНИЕ: Среднее значение — это число, которое представляет собой арифметическое среднее всех измерений.")
    print("Среднее значение можно найти по формуле: \n")
    print("  Среднее = (Сумма всех измерений) / (Количество измерений)")
    print("Теперь давайте вычислим среднее значение для набора ваших данных.")
    print("Для этого вам нужно будет ввести несколько измерений.")

# Функция для получения данных от пользователя
def get_measurements():
    while True:
        try:
            num_measurements = int(input("Введите количество измерений (от 1 до 10): "))
            if num_measurements < 1 or num_measurements > 10:
                print("❌ Ошибка: Введите количество измерений от 1 до 10!")
                continue
            break
        except ValueError:
            print("❌ Ошибка: Введите число!")

    measurements = []
    for i in range(num_measurements):
        while True:
            try:
                measurement = float(input(f"Введите измерение {i+1}: "))
                measurements.append(measurement)
                break
            except ValueError:
                print("❌ Ошибка: Введите число!")

    return measurements

# Функция для вычисления среднего значения
def calculate_average(measurements):
    total = sum(measurements)
    average = total / len(measurements)
    return average

# Функция проверки ответа с кнопкой
def check_answer():
    try:
        while True:
            explain_average()  # Объясняем среднее значение
            measurements = get_measurements()  # Получаем измерения от пользователя

            # Вычисляем среднее значение
            average = calculate_average(measurements)
            print(f"\nСреднее значение ваших измерений: {average:.2f}")
            print("Теперь попробуем сравнить ваше расчетное значение с правильным ответом!")

            print("Нажмите кнопку для проверки ответа...")
            while button.value():  # Ждём нажатия кнопки
                time.sleep(0.1)

            # Пояснение результата
            print(f"ℹ️ Среднее значение вычисляется по формуле: (Сумма всех измерений) / (Количество измерений).")
            print(f"ℹ️ Например, если ваши измерения: {measurements}, то (Сумма: {sum(measurements)}) / (Количество: {len(measurements)}) = {average:.2f}.")

            if average:
                show_color((0, 255, 0))  # Зеленый цвет
                print("✅ Все верно! Вы успешно вычислили среднее значение!")
            else:
                show_color((255, 0, 0))  # Красный цвет
                print(f"❌ Ошибка! Попробуйте еще раз. Правильное среднее значение: {average:.2f}")

            time.sleep(1)  # Даем время посмотреть результат
            show_color((0, 0, 0))  # Выключаем светодиоды
            print("\nСледующий расчет...\n")

    except KeyboardInterrupt:
        print("\n🚪 Выход из программы. До свидания!")
        show_color((0, 0, 0))  # Выключаем светодиоды перед выходом

# Основная программа
check_answer()  # Запускаем процесс вычисления среднего значения
