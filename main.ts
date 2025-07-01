input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    singBirthday()
})
input.onButtonPressed(Button.A, function () {
    if (isSingingBirthday != 1) {
        if (lighted_leds[position_horizontal][position_verticle] == 0) {
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.JumpUp), music.PlaybackMode.InBackground)
        }
        lighted_leds[position_horizontal][position_verticle] = 1
    }
})
input.onGesture(Gesture.LogoUp, function () {
    if (isSingingBirthday != 1) {
        led.unplot(position_horizontal, position_verticle)
        if (position_verticle < 4) {
            position_verticle = position_verticle + 1
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.BaDing), music.PlaybackMode.InBackground)
        }
    }
})
input.onGesture(Gesture.TiltLeft, function () {
    if (isSingingBirthday != 1) {
        led.unplot(position_horizontal, position_verticle)
        if (position_horizontal > 0) {
            position_horizontal = position_horizontal - 1
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.BaDing), music.PlaybackMode.InBackground)
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    if (isSingingBirthday != 1) {
        if (shouldCoursorBlink == 1) {
            shouldCoursorBlink = 0
        } else {
            shouldCoursorBlink = 1
        }
    }
})
input.onButtonPressed(Button.B, function () {
    if (isSingingBirthday != 1) {
        if (lighted_leds[position_horizontal][position_verticle] == 1) {
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.JumpDown), music.PlaybackMode.InBackground)
        }
        lighted_leds[position_horizontal][position_verticle] = 0
    }
})
input.onGesture(Gesture.Shake, function () {
    if (isSingingBirthday != 1) {
        resetScene()
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Punchline), music.PlaybackMode.InBackground)
    }
})
input.onGesture(Gesture.TiltRight, function () {
    if (isSingingBirthday != 1) {
        led.unplot(position_horizontal, position_verticle)
        if (position_horizontal < 5) {
            position_horizontal = position_horizontal + 1
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.BaDing), music.PlaybackMode.InBackground)
        }
    }
})
input.onGesture(Gesture.LogoDown, function () {
    if (isSingingBirthday != 1) {
        led.unplot(position_horizontal, position_verticle)
        if (position_verticle > 0) {
            position_verticle = position_verticle - 1
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.BaDing), music.PlaybackMode.InBackground)
        }
    }
})
function singBirthday () {
    isSingingBirthday = 1
    basic.clearScreen()
    basic.pause(40)
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Birthday), music.PlaybackMode.LoopingInBackground)
    basic.showString("HAPPY B'DAY RUHI")
    for (let index = 0; index < 3; index++) {
        basic.showIcon(IconNames.Heart)
        basic.pause(40)
        basic.showIcon(IconNames.SmallHeart)
        basic.pause(40)
    }
    basic.showLeds(`
        # . # # #
        # . # . #
        # . # . #
        # . # . #
        # . # # #
        `)
    basic.pause(2000)
    music.stopAllSounds()
    basic.clearScreen()
    isSingingBirthday = 0
}
function resetScene () {
    lighted_leds = [
    [
    0,
    0,
    0,
    0,
    0
    ],
    [
    0,
    0,
    0,
    0,
    0
    ],
    [
    0,
    0,
    0,
    0,
    0
    ],
    [
    0,
    0,
    0,
    0,
    0
    ],
    [
    0,
    0,
    0,
    0,
    0
    ]
    ]
    position_verticle = 2
    position_horizontal = 2
    basic.clearScreen()
    music.setVolume(50)
    shouldCoursorBlink = 1
}
let i = 0
let shouldCoursorBlink = 0
let position_verticle = 0
let position_horizontal = 0
let lighted_leds: number[][] = []
let isSingingBirthday = 0
singBirthday()
resetScene()
basic.forever(function () {
    let j: number;
if (isSingingBirthday == 1) {
        basic.pause(500)
    } else {
        basic.clearScreen()
        i = 0
        while (i < 5) {
            j = 0
            while (j < 5) {
                if (lighted_leds[i][j] == 1) {
                    led.plotBrightness(i, j, 50)
                }
                j = j + 1
            }
            i = i + 1
        }
        basic.pause(400)
    }
})
basic.forever(function () {
    if (isSingingBirthday == 1) {
        basic.pause(500)
    } else if (shouldCoursorBlink == 1) {
        basic.pause(50)
        led.plotBrightness(position_horizontal, position_verticle, 255)
        basic.pause(200)
        if (lighted_leds[position_horizontal][position_verticle] == 1) {
            led.plotBrightness(position_horizontal, position_verticle, 50)
        } else {
            led.unplot(position_horizontal, position_verticle)
        }
    } else {
    	
    }
})
