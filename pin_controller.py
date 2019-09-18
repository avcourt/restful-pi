import RPi.GPIO as GPIO

pins = [{'pin_num': 23, 'color': 'red'},
        {'pin_num': 24, 'color': 'yellow'},
        {'pin_num': 25, 'color': 'blue'},
        {'pin_num': 22, 'color': 'red'},
        {'pin_num': 12, 'color': 'yellow'},
        {'pin_num': 16, 'color': 'blue'},
        {'pin_num': 20, 'color': 'red'},
        {'pin_num': 21, 'color': 'green'},
        {'pin_num': 13, 'color': 'yellow'}]

GPIO.setmode(GPIO.BCM)  # use GPIO numbering, not generic

# setup all pins based on above configuration
for pin in pins:
    GPIO.setup(pin['pin_num'], GPIO.OUT, initial=GPIO.LOW)


def toggle_color(color: str, state: str):
    pin_nums = [pin['pin_num'] for pin in pins if pin['color'] == color]
    for pin_num in pin_nums:
        if state == 'on':
            GPIO.output(pin_num, GPIO.HIGH)
        elif state == 'off':
            GPIO.output(pin_num, GPIO.LOW)


def color_on(color: str):
    toggle_color(color, 'on')


def color_off(color: str):
    toggle_color(color, 'off')


def all_on():
    for pin in pins:
        GPIO.output(pin['pin_num'], GPIO.HIGH)


def all_off():
    for pin in pins:
        GPIO.output(pin['pin_num'], GPIO.LOW)


def pin_on(pin_num: int):
    GPIO.output(pin_num, GPIO.HIGH)


def pin_off(pin_num: int):
    GPIO.output(pin_num, GPIO.LOW)