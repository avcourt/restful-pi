# RESTful PI
This is a Flask app written in Python3. This app is REST backend to control the GPIO pins (turn on and off LEDs) of a Raspberry Pi by making HTTP requests to the `/pins` and `/pins/<id>` endpoints of the Flask webserver.

These requests use the standard HTTP requests `GET`, `POST`, `PUT`, and `DELETE`.

The JSON model of the `pin` resource is:
```json 
    {
        "id": "Integer(readonly=True, description='The pin unique identifier')",
        "pin_num": "Integer(required=True, description='GPIO pin associated with this endpoint')",
        "color": "String(required=True, description='LED color')",
        "state": "String(required=True, description='LED on or off')"
    }
```

The 4 HTTP verbs correspond to the typical CRUD operations:
- POST `pins/` : **Create** a new pin
    - where the posted data is JSON looking somethign like the following:
        ```
        {
            "pin_num": 23,
            "color": "red,
            "state": "on"
        }
        ```
- GET `pins/`: Fetech (**Read**) all pins stored on the system
    - e.g:
      ```
        {
            "id: "1",
            "pin_num": 23,
            "color": "red,
            "state": "on"
        },
        {
            "id": "2",
            "pin_num": 24,
            "color": "blue,
            "state": "off"
        }
        ```
 - GET `pins/<id>`: Fetch a pin given its resource identifier
    - e.g. GET `pins/2`:
    ```
        {
            "id": "2",
            "pin_num": 24,
            "color": "blue,
            "state": "off"
        }
    ```

