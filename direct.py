import RPi.GPIO as GPIO
import random
import time

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

pins = [{'id': 23, 'color': 'red'},
        {'id': 24, 'color': 'yellow'},
        {'id': 25, 'color': 'blue'},
        {'id': 22, 'color': 'red'},
        {'id': 12, 'color': 'yellow'},
        {'id': 16, 'color': 'blue'},
        {'id': 20, 'color': 'red'},
        {'id': 21, 'color': 'green'},
        {'id': 13, 'color': 'yellow'}]


def toggle_color(color: str):

    switch_pins = [pin['id'] for pin in pins if pin['color'] == color]

    for pin in switch_pins:
        if GPIO.input(pin):
            GPIO.output(pin['id'], GPIO.LOW)
        else:
            GPIO.output(pin['id'], GPIO.HIGH)


def pin_on(pin_num: int):
    GPIO.output(pin_num, GPIO.HIGH)

def pin_off(pin_num: int):
    GPIO.output(pin_num, GPIO.LOW)


def all_on():
    for pin in pins:
        GPIO.output(pin['id'], GPIO.HIGH)


def all_off():
    for pin in pins:
        GPIO.output(pin['id'], GPIO.LOW)

def switch_all(state: str):
    if state == "on":
        all_on()
    elif state == "off":
        all_off()
    else:
        print("Error: switch_all() expects str 'on' of 'off'")




