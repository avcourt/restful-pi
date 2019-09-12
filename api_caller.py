import requests
import random
import time

from urllib.parse import urljoin

HOST = 'http://localhost:5000'
PIN_ENDPOINT = 'pins/'
PINS = urljoin(HOST, PIN_ENDPOINT)


def toggle_color(color: str, state: str):
    pins = requests.get(PINS).json()

    switch_pins = [pin['id'] for pin in pins if pin['color'] == color]

    for pin in switch_pins:
        requests.patch(urljoin(PINS, str(pin)),
                     json={"state": state})


def switch_all(state: str):
    pins = requests.get(PINS).json()

    for pin in pins:
        if pin['state'] != state:
            requests.patch(urljoin(PINS, str(pin['id'])),
                         json={"state": state})


def all_on():
    switch_all("on")


def all_off():
    switch_all("off")


def color_on(color: str):
    toggle_color(color, 'on')


def color_off(color: str):
    toggle_color(color, 'off')


def random_stuff(max_period=0.5):
    all_list = [all_on, all_off]
    color_functs = [color_off, color_on]

    colors = ['red', 'blue', 'green', 'yellow']

    while True:
        random.choice(all_list)()
        time.sleep(random.uniform(0.1, max_period))
        random.choice(color_functs)(random.choice(colors))
        time.sleep(random.uniform(0.1, max_period))
        random.choice(color_functs)(random.choice(colors))
        time.sleep(random.uniform(0.1, max_period))


def rainbow(period=0.5):
    colors = ['red', 'blue', 'green', 'yellow']
    while True:
        for color in colors:
            color_on(color)
            time.sleep(period)
            color_off(color)


def on_off(period=0.5):
    while True:
        all_on()
        time.sleep(period)
        all_off()
        time.sleep(period)


def wave(period=0.1):
    while True:
        pins = requests.get(PINS).json()

        for pin in pins:
            requests.patch(urljoin(PINS, str(pin['id'])),
                         json={"state": "on"})
            time.sleep(period)

        for pin in reversed(pins):
            requests.patch(urljoin(PINS, str(pin['id'])),
                         json={"state": "off"})
            time.sleep(period)


def single_rand(period=0.1):
    while True:
        pins = requests.get(PINS).json()
        pin = random.choice(pins)
        requests.patch(urljoin(PINS, str(pin['id'])),
                     json={"state": "on"})
        time.sleep(period)
        requests.patch(urljoin(PINS, str(pin['id'])),
                     json={"state": "off"})


if __name__ == '__main__':
    # random_stuff()
    rainbow()
