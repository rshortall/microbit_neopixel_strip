strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P2, 30, NeoPixelMode.RGB)

window1 = strip.range(0, 1)
window2 = strip.range(1, 1)
window3 = strip.range(2, 1)
window4 = strip.range(3, 1)
window5 = strip.range(4, 1)

window1.show_color(neopixel.hsl(5, 100, 50))
window2.show_color(neopixel.hsl(20, 100, 51))
window3.show_color(neopixel.hsl(50, 100, 50))
window4.show_color(neopixel.hsl(20, 100, 51))
window5.show_color(neopixel.hsl(5, 100, 50))

def on_button_pressed_a():
    bounceLights()
    basic.pause(1000)
    bounceRainbow()

input.on_button_pressed(Button.A, on_button_pressed_a)

def on_sound_loud():
    bounceLights()
    basic.pause(1000)
    bounceRainbow()

input.on_sound(DetectedSound.LOUD, on_sound_loud)

def bounceLights():
    for index in range(5):
        for index2 in range(25):
            strip.rotate(1)
            strip.show()
            basic.pause(100)
        for index3 in range(25):
            strip.rotate(-1)
            strip.show()
            basic.pause(100)

def on_button_pressed_b():
    strip.clear()
    strip.show()

input.on_button_pressed(Button.B, on_button_pressed_b)

def bounceRainbow():
    strip.show_rainbow(1, 360)
    for index4 in range(4):
        for index5 in range(31):
            strip.rotate(1)
            strip.show()
            basic.pause(100)