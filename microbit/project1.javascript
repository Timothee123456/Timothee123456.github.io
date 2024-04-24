input.onButtonPressed(Button.A, function () {
    if (number != 1) {
        number += -1
        basic.showNumber(number)
    }
})
input.onButtonPressed(Button.AB, function () {
    strip.setPixelColor(number - 1, neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
    strip.show()
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    control.waitMicros(4)
    basic.showNumber(number)
})
input.onButtonPressed(Button.B, function () {
    if (number != 30) {
        number += 1
        basic.showNumber(number)
    }
})
let number = 0
let strip: neopixel.Strip = null
let Item = 0
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip.showRainbow(1, 360)
number = 1
basic.showNumber(number)
