let item = 0
let strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip.showRainbow(1, 360)
strip.show()
basic.forever(function () {
    item = randint(0, 30)
    strip.setPixelColor(item, neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
    strip.show()
    basic.showNumber(randint(0, 9))
})
