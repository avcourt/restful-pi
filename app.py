from flask import Flask
from flask_restplus import Api, Resource, fields
import RPi.GPIO as GPIO


app = Flask(__name__)
api = Api(app,
          version='1.0',
          title='RESTful Pi',
          description='A RESTful API to control the GPIO pins of a Raspbery Pi',
          doc='/docs')

ns = api.namespace('pins', description='Pin related operations')

pin_model = api.model('pins', {
    'id': fields.Integer(readonly=True, description='The pin unique identifier'),
    'pin_num': fields.Integer(required=True, description='GPIO pin associated with this endpoint'),
    'color': fields.String(required=True, description='LED color'),
    'state': fields.String(required=True, description='LED on or off')
})


class PinUtil(object):
    def __init__(self):
        self.counter = 0
        self.pins = []

    def get(self, id):
        for pin in self.pins:
            if pin['id'] == id:
                return pin
        api.abort(404, f"pin {id} doesn't exist.")

    def create(self, data):
        pin = data
        pin['id'] = self.counter = self.counter + 1
        self.pins.append(pin)
        GPIO.setup(pin['pin_num'], GPIO.OUT)

        if pin['state'] == 'off':
            GPIO.output(pin['pin_num'], GPIO.LOW)
        elif pin['state'] == 'on':
            GPIO.output(pin['pin_num'], GPIO.HIGH)

        return pin

    def update(self, id, data):
        pin = self.get(id)
        pin.update(data)  # this is the dict_object update method
        GPIO.setup(pin['pin_num'], GPIO.OUT)

        if pin['state'] == 'off':
            GPIO.output(pin['pin_num'], GPIO.LOW)
        elif pin['state'] == 'on':
            GPIO.output(pin['pin_num'], GPIO.HIGH)

        return pin

    def delete(self, id):
        pin = self.get(id)
        GPIO.output(pin['pin_num'], GPIO.LOW)
        self.pins.remove(pin)


@ns.route('/')  # keep in mind this our ns-namespace (pins/)
class PinList(Resource):
    """Shows a list of all pins, and lets you POST to add new pins"""

    @ns.marshal_list_with(pin_model)
    def get(self):
        """List all pins"""
        return pin_util.pins

    @ns.expect(pin_model)
    @ns.marshal_with(pin_model, code=201)
    def post(self):
        """Create a new pin"""
        return pin_util.create(api.payload)


@ns.route('/<int:id>')
@ns.response(404, 'pin not found')
@ns.param('id', 'The pin identifier')
class Pin(Resource):
    """Show a single pin item and lets you update/delete them"""

    @ns.marshal_with(pin_model)
    def get(self, id):
        """Fetch a pin given its resource identifier"""
        return pin_util.get(id)

    @ns.response(204, 'pin deleted')
    def delete(self, id):
        """Delete a pin given its identifier"""
        pin_util.delete(id)
        return '', 204

    @ns.expect(pin_model, validate=True)
    @ns.marshal_with(pin_model)
    def put(self, id):
        """Update a pin given its identifier"""
        return pin_util.update(id, api.payload)
    
    @ns.expect(pin_model)
    @ns.marshal_with(pin_model)
    def patch(self, id):
        """Partially update a pin given its identifier"""
        return pin_util.update(id, api.payload)


GPIO.setmode(GPIO.BCM)

pin_util = PinUtil()
pin_util.create({'pin_num': 23, 'color': 'red', 'state': 'off'})
pin_util.create({'pin_num': 24, 'color': 'yellow', 'state': 'off'})
pin_util.create({'pin_num': 25, 'color': 'blue', 'state': 'off'})
pin_util.create({'pin_num': 22, 'color': 'red', 'state': 'off'})
pin_util.create({'pin_num': 12, 'color': 'yellow', 'state': 'off'})
pin_util.create({'pin_num': 16, 'color': 'blue', 'state': 'off'})
pin_util.create({'pin_num': 20, 'color': 'red', 'state': 'off'})
pin_util.create({'pin_num': 21, 'color': 'green', 'state': 'off'})
pin_util.create({'pin_num': 13, 'color': 'yellow', 'state': 'off'})


if __name__ == '__main__':
    app.run(debug=True)
