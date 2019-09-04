import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)

pins = [{'pin_num': 23, 'color': 'red'},
        {'pin_num': 24, 'color': 'yellow'},
        {'pin_num': 25, 'color': 'blue'},
        {'pin_num': 22, 'color': 'red'},
        {'pin_num': 12, 'color': 'yellow'},
        {'pin_num': 16, 'color': 'blue'},
        {'pin_num': 20, 'color': 'red'},
        {'pin_num': 21, 'color': 'green'},
        {'pin_num': 13, 'color': 'yellow'}]


def color_on(color: str):
	pin_nums = [pin['pin_num'] for pin in pins if pin['color'] == color]
	for pin_num in pin_nums:
		GPIO.output(pin_num, GPIO.HIGH)


def color_off(color: str):
	pin_nums = [pin['pin_num'] for pin in pins if pin['color'] == color]
	for pin_num in pin_nums:
		GPIO.output(pin_num, GPIO.LOW)


def pin_on(pin_num: int):
    GPIO.output(pin_num, GPIO.HIGH)


def pin_off(pin_num: int):
    GPIO.output(pin_num, GPIO.LOW)


def all_on():
    for pin in pins:
        GPIO.output(pin['pin_num'], GPIO.HIGH)


def all_off():
    for pin in pins:
        GPIO.output(pin['pin_num'], GPIO.LOW)


def switch_all(state: str):
    if state == "on":
        all_on()
    elif state == "off":
        all_off()
    else:
        print("Error: switch_all() expects str 'on' or 'off'")




