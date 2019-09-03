# RESTful Pi
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
        ```json
        {
            "pin_num": 23,
            "color": "red",
            "state": "on"
        }
        ```
- GET `pins/`: Fetech (**Read**) all pins stored on the system
    - e.g:
      ```json
        {
            "id": "1",
            "pin_num": 23,
            "color": "red",
            "state": "on"
        },
        {
            "id": "2",
            "pin_num": 24,
            "color": "blue",
            "state": "off"
        }
        ```
 - GET `pins/<id>`: Fetch a pin given its resource identifier
    - e.g. GET `pins/2`:
    ```json
        {
            "id": "2",
            "pin_num": 24,
            "color": "blue",
            "state": "off"
        }
    ```
 - PUT `pins/<id>` : **Update** a pin given its resource id
    - You can update a single field, or all fields (except for its uid which is READONLY)
    - e.g. Update the state of pin with id 2:
        - PUT `/pins/2` 
            ```json
            {"state": "off"}
            ```
     - e.g. Update all fields of pin with id 2:
        - PUT `/pins/2` 
            ```json
            {
                "pin_num": 24,
                "color": "blue",
                "state": "off"
            }
            ```
 - DELETE `pins/<id>` : **Delete** pin<id> from system
    
## Breadboard Setup
For this project to work without modifying the code, you will need:
- 9 x (preferably multicolored leds, 3xR,1xG,2xB,3xY in my case)
- 9 x 1k resistors (anything over 100Ω should be fine)
- 1 x breadboard
- 10 x GPIO connecting cables

There are many kits available on Amazon for under $20.
    
### Schematic
```json
{"pin_num": 23, "color": "red",}
{"pin_num": 24, "color": "yellow"},
{"pin_num": 25, "color": "blue"},
{"pin_num": 22, "color": "red"},
{"pin_num": 12, "color": "yellow"},
{"pin_num": 16, "color": "blue"},
{"pin_num": 20, "color": "red"},
{"pin_num": 21, "color": "green"},
{"pin_num": 13, "color": "yellow"}
```
