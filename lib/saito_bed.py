from lib.simple_mqtt_client import *
from lib.effects.color_effect import *
from lib.effects.nightrider_effect import *
from lib.effects.rainbow_effect import *
from lib.effect_manager import *
from uuid import getnode as get_mac
import json
from jsonschema import validate
from jsonschema import exceptions

neopixel_schema = {
    "type" : "object",
    "properties" : {
        "state" : {"enum" : ["ON", "OFF"]},
        "effect" : {"enum" : ["rainbow", "nightrider"]},
        "brightness" : {"type": "number", "minimum": 0, "maximum": 255 },
        "color": {
            "type" : "object",
            "properties" : {
                "r" : {"type": "number", "minimum": 0, "maximum": 255 },
                "g" : {"type": "number", "minimum": 0, "maximum": 255 },
                "b" : {"type": "number", "minimum": 0, "maximum": 255 }
            },
            "required": ["r", "g", "b"]
        }
    }
}

class SaitoBed(object):
    def __init__(self, pixelStrip, mqttBroker, baseTopic="saito/bed"):
        self.pixelStrip = pixelStrip
        self.mqttBroker = mqttBroker
        self.baseTopic = baseTopic
        self.effectManager = EffectManager(pixelStrip)
        self.effectManager.set_effect(ColorEffect(pixelStrip, Colors.BLACK))
        self.effectManager.disable()
        self.__setup_mqtt()

    def stop(self):
        print("Stopping MQTT API")
        self.mqttClient.stop()

    def __setup_mqtt(self):
        clientId = str(get_mac()) + "-python_client"
        self.mqttClient = SimpleMqttClient(clientId, self.mqttBroker)
        self.mqttClient.subscribe(self.baseTopic + "/neopixels/set", self.__mqtt_message_handler)
        sleep(2)
        self.__publish_pixelstrip_state()       # For Home Assistant

    def __mqtt_message_handler(self, client, userdata, msg):
        print("Getting set neopixels request: " + msg.payload.decode('utf-8'))
        self.__set_neopixels(msg.payload.decode('utf-8'))
        self.__publish_pixelstrip_state()       # For Home Assistant

    # TODO: Needs to be refactored, not ok
    def __set_neopixels(self, jsonString):
        try:
            jsonData = json.loads(jsonString)
            # If no exception is raised by validate(), the instance is valid.
            validate(jsonData, neopixel_schema)

            print(jsonData)

            if 'state' in jsonData:
                if jsonData['state'] == 'ON':
                    self.effectManager.enable()
                elif jsonData['state'] == 'OFF':
                    self.effectManager.disable()

            if len(jsonData.keys()) > 1:
                previousEffect = self.effectManager.get_current_effect()
                effect = ColorEffect(self.pixelStrip, previousEffect.get_color(), previousEffect.get_brightness())

                if ('effect' in jsonData) and (jsonData['effect'] == 'nightrider'):
                    effect = NightRiderEffect(self.pixelStrip, previousEffect.get_color(), previousEffect.get_brightness())
                elif ('effect' in jsonData) and (jsonData['effect'] == 'rainbow'):
                    effect = RainbowEffect(self.pixelStrip, previousEffect.get_brightness())

                if 'color' in jsonData:
                    components = jsonData['color']
                    color = Color(components['r'], components['g'], components['b'])
                    effect.set_color(color)

                if ('brightness' in jsonData):
                    effect.set_brightness(jsonData['brightness'])

                self.effectManager.set_effect(effect)

        except exceptions.ValidationError:
            print("Message failed validation")
        except ValueError:
            print("Invalid json string")

    def __publish_pixelstrip_state(self):
        state = self.__get_pixelstrip_state()
        (status, mid) = self.mqttClient.publish(self.baseTopic + "/neopixels", state)
        if status != 0:
            print("Could not send state")

    def __get_pixelstrip_state(self):
        json_state = {
            "brightness": self.effectManager.get_current_effect().get_brightness(),
            "state": "ON" if self.effectManager.is_enabled() else "OFF",
            "color": {
                "r": self.effectManager.get_current_effect().get_color().red(),
                "g": self.effectManager.get_current_effect().get_color().green(),
                "b": self.effectManager.get_current_effect().get_color().blue()
            }
        }

        if isinstance(self.effectManager.get_current_effect(), NightRiderEffect):
            json_state['effect'] = 'nightrider'
        elif isinstance(self.effectManager.get_current_effect(), RainbowEffect):
            json_state['effect'] = 'rainbow'

        return json.dumps(json_state)
