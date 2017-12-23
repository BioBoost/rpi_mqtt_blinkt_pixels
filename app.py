from time import sleep
import sys
from lib.pixel_strip import *
from lib.color import *
from lib.simple_mqtt_client import *
from lib.effects.color_effect import *
from lib.effects.nightrider_effect import *
from lib.effect_manager import *

BROKER_ADDRESS = "10.0.0.100"

def mqtt_message_handler(client, userdata, msg):
    print("Received: " + msg.payload.decode('utf-8'))

if __name__ == '__main__':
    strip = PixelStrip()
    colorEffect = ColorEffect(strip, Colors.RED)
    nightRider = NightRiderEffect(strip, Colors.YELLOW, 0.1)

    effectManager = EffectManager(strip)
    effectManager.set_effect(nightRider)

    mqttClient = SimpleMqttClient("notreggsdf4323423", BROKER_ADDRESS)
    mqttClient.subscribe("some/other/random/topic", mqtt_message_handler)

    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:       # Catch CTRL-C
        mqttClient.stop()
        print ("Bye Bye")
        sys.exit()
