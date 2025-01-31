import array, time
from machine import Pin
import rp2

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

class ws2812b:
    def __init__(self, pin, state_machine=0, delay=0.001):
        # Массив теперь только для одного пикселя
        self.pixels = array.array("I", [0])  # Только один пиксель
        self.sm = rp2.StateMachine(state_machine, ws2812, freq=8000000, sideset_base=Pin(pin))
        self.sm.active(1)
        self.delay = delay
        self.brightnessvalue = 255

    # Установка яркости
    def brightness(self, brightness=None):
        if brightness is None:
            return self.brightnessvalue
        else:
            if brightness < 1:
                brightness = 1
            if brightness > 255:
                brightness = 255
            self.brightnessvalue = brightness

    # Установка значения одного пикселя
    def set_pixel(self, red, green, blue):
        # Применение яркости
        blue = round(blue * (self.brightness() / 255))
        red = round(red * (self.brightness() / 255))
        green = round(green * (self.brightness() / 255))

        # Присваиваем цвет пикселю (работаем только с одним пикселем)
        self.pixels[0] = blue | red << 8 | green << 16

    # Показать пиксель
    def show(self):
        # Передаем данные только для одного пикселя
        self.sm.put(self.pixels[0], 8)
        time.sleep(self.delay)

 