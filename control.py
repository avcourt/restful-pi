import requests
import random
import time

from urllib.parse import urljoin

HOST = 'http://localhost:5000'


def toggle_color(color: str, on_off: str):
    pins = requests.get(urljoin(HOST, 'pins')).json()

    switch_pins = [pin['id'] for pin in pins if pin['color'] == color]

    for pin in switch_pins:
        requests.put(urljoin(HOST, f"pins/{str(pin)}"),
                     json={"state": on_off})


def switch_all(state: str):
    pins = requests.get(urljoin(HOST, 'pins')).json()

    for pin in pins:
        if pin['state'] != state:
            requests.put(urljoin(HOST, f"pins/{str(pin['id'])}"),
                         json={"state": state})


def all_on():
    switch_all("on")


def all_off():
    switch_all("off")


def color_on(color: str):
    toggle_color(color, 'on')


def color_off(color: str):
    toggle_color(color, 'off')


def random_stuff():
    all_list = [all_on, all_off]
    color_functs = [color_off, color_on]

    colors = ['red', 'blue', 'green', 'yellow']

    while True:
        random.choice(all_list)
        time.sleep(0.3)
        random.choice(color_functs)(random.choice(colors))
        time.sleep(0.2)
        random.choice(color_functs)(random.choice(colors))
        time.sleep(0.5)


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
        pins = requests.get(urljoin(HOST, 'pins')).json()

        for pin in pins:
            requests.put(urljoin(HOST, f"pins/{str(pin['id'])}"),
                         json={"state": "on"})
            time.sleep(period)

            for pin in pins:
                requests.put(urljoin(HOST, f"pins/{str(pin['id'])}"),
                             json={"state": "on"})
                time.sleep(period)

            for pin in reversed(pins):
                requests.put(urljoin(HOST, f"pins/{str(pin['id'])}"),
                             json={"state": "off"})
                time.sleep(period)


def single_rand(period=0.1):
    pins = requests.get(urljoin(HOST, 'pins')).json()

    while True:  # assume no pins are changed while running this func
        pin = random.choice(pins)
        requests.put(urljoin(HOST, f"pins/{str(pin['id'])}"),
                     json={"state": "on"})
        time.sleep(period)
        requests.put(urljoin(HOST, f"pins/{str(pin['id'])}"),
                     json={"state": "off"})


if __name__ == '__main__':
    # random_stuff()
    rainbow()
