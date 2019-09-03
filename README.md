# RESTful PI
This is a Flask app written in Python3. This app is REST backend to control the GPIO pins (turn on and off lights) of a Raspberry Pi by making HTTP requests to the `/pins` and `/pins/<id>` endpoints of the Flask webserver.

These requests use the standard HTTP requests `GET`, `POST`, `PUT`, and `DELETE`.

The JSON model of the `pin` resource is:
```json 
    'id': fields.Integer(readonly=True, description='The pin unique identifier'),
    'pin_num': Integer(required=True, description='GPIO pin associated with this endpoint'),
    'color': String(required=True, description='LED color'),
    'state': String(required=True, description='LED on or off')
```

