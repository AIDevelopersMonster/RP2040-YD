import math

# Словарь с описанием модулей и функций
modules = {
    'math': {
        'description': 'Модуль math предоставляет математические функции, такие как синусы, косинусы, логарифмы и другие.',
        'functions': {
            '1': {
                'name': 'sqrt',
                'description': 'Возвращает квадратный корень из числа.',
                'example': 'Пример: math.sqrt(16)',
                'usage': 'Введите число, чтобы вычислить его квадратный корень.'
            },
            '2': {
                'name': 'pow',
                'description': 'Возвращает число, возведенное в степень.',
                'example': 'Пример: math.pow(2, 3) = 8',
                'usage': 'Введите число и степень, чтобы вычислить результат.'
            },
            # Можно добавить другие функции...
        }
    }
    # Можно добавить другие модули...
}

# Функция для вывода списка доступных модулей
def display_modules():
    print("Доступные модули: ")
    for i, module in enumerate(modules.keys(), 1):
        print(f"{i}. {module}")

# Функция для вывода списка функций модуля
def display_functions(module_name):
    print(f"\nФункции модуля {module_name}:")
    for num, func in modules[module_name]['functions'].items():
        print(f"{num}. {func['name']}")

# Функция для отображения описания функции
def display_function_details(module_name, func_number):
    func = modules[module_name]['functions'][str(func_number)]  # Используем str для ключа
    print(f"\nФункция {func['name']}:")
    print(f"Описание: {func['description']}")
    print(f"Пример использования: {func['example']}")
    print(f"Интерактивное использование: {func['usage']}")

# Функция для выполнения примера функции
def interactive_example(module_name, func_number):
    func = modules[module_name]['functions'][str(func_number)]  # Используем str для ключа
    
    if func['name'] == 'sqrt':
        number = float(input("Введите число для вычисления квадратного корня: "))
        print(f"Квадратный корень из {number} = {math.sqrt(number)}")
    elif func['name'] == 'pow':
        base = float(input("Введите основание (число): "))
        exponent = float(input("Введите степень: "))
        print(f"{base} в степени {exponent} = {math.pow(base, exponent)}")
    # Можно добавить обработку для других функций...

# Основная функция
def main():
    print("Добро пожаловать в справочник по математическим функциям!")
    
    while True:
        display_modules()
        module_choice = int(input("Выберите модуль (введите номер) или 0 для выхода: "))
        
        if module_choice == 0:
            break
        
        module_name = list(modules.keys())[module_choice - 1]
        print(f"\nВы выбрали модуль {module_name}.")
        
        display_functions(module_name)
        func_choice = int(input("Выберите функцию (введите номер) или 0 для выхода: "))
        
        if func_choice == 0:
            break
        
        display_function_details(module_name, func_choice)
        
        interact = input("Хотите выполнить пример этой функции? (y/n): ").strip().lower()
        if interact == 'y':
            interactive_example(module_name, func_choice)

# Запуск программы
if __name__ == "__main__":
    main()
