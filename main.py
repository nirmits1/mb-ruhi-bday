def on_logo_long_pressed():
    singBirthday()
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    if isSingingBirthday != 1:
        if lighted_leds[position_horizontal][position_verticle] == 0:
            music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
                music.PlaybackMode.IN_BACKGROUND)
        lighted_leds[position_horizontal][position_verticle] = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    global position_verticle
    if isSingingBirthday != 1:
        led.unplot(position_horizontal, position_verticle)
        if position_verticle < 4:
            position_verticle = position_verticle + 1
            music._play_default_background(music.built_in_playable_melody(Melodies.BA_DING),
                music.PlaybackMode.IN_BACKGROUND)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    global position_horizontal
    if isSingingBirthday != 1:
        led.unplot(position_horizontal, position_verticle)
        if position_horizontal > 0:
            position_horizontal = position_horizontal - 1
            music._play_default_background(music.built_in_playable_melody(Melodies.BA_DING),
                music.PlaybackMode.IN_BACKGROUND)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    global shouldCoursorBlink
    if isSingingBirthday != 1:
        if shouldCoursorBlink == 1:
            shouldCoursorBlink = 0
        else:
            shouldCoursorBlink = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if isSingingBirthday != 1:
        if lighted_leds[position_horizontal][position_verticle] == 1:
            music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_DOWN),
                music.PlaybackMode.IN_BACKGROUND)
        lighted_leds[position_horizontal][position_verticle] = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    if isSingingBirthday != 1:
        resetScene()
        music._play_default_background(music.built_in_playable_melody(Melodies.PUNCHLINE),
            music.PlaybackMode.IN_BACKGROUND)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    global position_horizontal
    if isSingingBirthday != 1:
        led.unplot(position_horizontal, position_verticle)
        if position_horizontal < 5:
            position_horizontal = position_horizontal + 1
            music._play_default_background(music.built_in_playable_melody(Melodies.BA_DING),
                music.PlaybackMode.IN_BACKGROUND)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    global position_verticle
    if isSingingBirthday != 1:
        led.unplot(position_horizontal, position_verticle)
        if position_verticle > 0:
            position_verticle = position_verticle - 1
            music._play_default_background(music.built_in_playable_melody(Melodies.BA_DING),
                music.PlaybackMode.IN_BACKGROUND)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def singBirthday():
    global isSingingBirthday
    isSingingBirthday = 1
    basic.clear_screen()
    basic.pause(40)
    music.set_volume(50)
    music._play_default_background(music.built_in_playable_melody(Melodies.BIRTHDAY),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    basic.show_string("HAPPY B'DAY RUHI")
    for index in range(3):
        basic.show_icon(IconNames.HEART)
        basic.pause(40)
        basic.show_icon(IconNames.SMALL_HEART)
        basic.pause(40)
    basic.show_leds("""
        # . # # #
        # . # . #
        # . # . #
        # . # . #
        # . # # #
        """)
    basic.pause(2000)
    music.stop_all_sounds()
    basic.clear_screen()
    music.set_volume(50)
    isSingingBirthday = 0
def resetScene():
    global lighted_leds, position_verticle, position_horizontal, shouldCoursorBlink
    lighted_leds = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
        ]
    position_verticle = 2
    position_horizontal = 2
    basic.clear_screen()
    music.set_volume(50)
    shouldCoursorBlink = 1
i = 0
shouldCoursorBlink = 0
position_verticle = 0
position_horizontal = 0
lighted_leds: List[List[number]] = []
isSingingBirthday = 0
singBirthday()
resetScene()

def on_forever():
    global i
    if isSingingBirthday == 1:
        basic.pause(500)
    else:
        basic.clear_screen()
        i = 0
        while i < 5:
            j = 0
            while j < 5:
                if lighted_leds[i][j] == 1:
                    led.plot_brightness(i, j, 50)
                j = j + 1
            i = i + 1
        basic.pause(400)
basic.forever(on_forever)

def on_forever2():
    if isSingingBirthday == 1:
        basic.pause(500)
    elif shouldCoursorBlink == 1:
        basic.pause(50)
        led.plot_brightness(position_horizontal, position_verticle, 255)
        basic.pause(200)
        if lighted_leds[position_horizontal][position_verticle] == 1:
            led.plot_brightness(position_horizontal, position_verticle, 50)
        else:
            led.unplot(position_horizontal, position_verticle)
    else:
        pass
basic.forever(on_forever2)
