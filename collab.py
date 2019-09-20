import requests
import random
import time

from urllib.parse import urljoin

HOST = 'http://localhost:5000'
PIN_ENDPOINT = 'pins/'
PINS = urljoin(HOST, PIN_ENDPOINT)


def toggle_color(color: str, state: str):
    for pin in requests.get(PINS).json():
        if pin['color'] == color:
            requests.patch(urljoin(PINS, str(pin)),
                           json={"state": state})


def switch_all(state: str):
    for pin in requests.get(PINS).json():
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