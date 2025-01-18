# Video https://youtu.be/-b29zY6aEKs
# Post http://kontakts.ru/showthread.php/40884?p=86155#post86155
from machine import Pin
import tm1637
from utime import sleep, ticks_ms

tm = tm1637.TM1637(clk=Pin(4), dio=Pin(5))
RoA_Pin = 0    # CLK
RoB_Pin = 1    # DT
Btn_Pin = 2    # SW

globalCounter = 0  # counter value

flag = 0                # Whether the rotation flag occurs
Last_RoB_Status = 0     # DT state
Current_RoB_Status = 0  # CLK state

# Переменные для дебаунса
debounceDelay = 100  # Задержка для дебаунса в миллисекундах
lastDebounceTime = 0  # Время последнего изменения состояния кнопки
lastBtnState = 1      # Предыдущее состояние кнопки

def setup():
    global clk_RoA
    global dt_RoB
    global sw_BtN
    
    clk_RoA = Pin(RoA_Pin, Pin.IN) 
    dt_RoB = Pin(RoB_Pin, Pin.IN)   
    sw_BtN = Pin(Btn_Pin, Pin.IN, Pin.PULL_UP) 
    # Инициализация прерывания для кнопки
    sw_BtN.irq(trigger=Pin.IRQ_FALLING, handler=btnISR)

# Функция для обработки поворота энкодера
def rotaryDeal():
    global flag
    global Last_RoB_Status
    global Current_RoB_Status
    global globalCounter

    Last_RoB_Status = dt_RoB.value()
    # Проверка уровня сигнала на CLK, чтобы различить направление
    while not clk_RoA.value():
        Current_RoB_Status = dt_RoB.value()
        flag = 1  # Флаг срабатывания вращения
    if flag == 1:
        flag = 0  # Сброс флага
        if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
            globalCounter += 1  # Против часовой стрелки, увеличение
        if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
            globalCounter -= 1  # По часовой стрелке, уменьшение

# Функция обработки нажатия кнопки с дебаунсом
def btnISR(chn):
    global globalCounter, lastBtnState, debounceDelay, lastDebounceTime

    currentBtnState = sw_BtN.value()  # Получаем текущее состояние кнопки

    # Проверяем, прошло ли достаточно времени для дебаунса
    if currentBtnState != lastBtnState:
        lastDebounceTime = ticks_ms()  # Обновляем время последнего изменения состояния кнопки

    # Если прошло достаточно времени (с момента последнего изменения состояния), обновляем счётчик
    if (ticks_ms() - lastDebounceTime) > debounceDelay:
        if currentBtnState == 0:  # Если кнопка нажата
            print(f'Вы выбрали значение: {globalCounter}')  # Выводим выбранное значение
            tm.number(globalCounter)  # Отображаем значение на дисплее

    lastBtnState = currentBtnState  # Обновляем предыдущее состояние кнопки

def loop():
    global globalCounter  
    tmp = 0   
    while True:
        rotaryDeal()      
        if tmp != globalCounter: 
            print(f'globalCounter = {globalCounter}')  # Печатаем в консоль
            tmp = globalCounter    
            tm.number(globalCounter)  # Обновляем дисплей

if __name__ == '__main__':    
    setup() 
    loop()
