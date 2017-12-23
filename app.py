from time import sleep
import sys
from lib.pixel_strip import *
from lib.color import *
from lib.simple_mqtt_client import *
from lib.effects.color_effect import *

BROKER_ADDRESS = "10.0.0.100"

def mqtt_message_handler(client, userdata, msg):
    print("Received: " + msg.payload.decode('utf-8'))

if __name__ == '__main__':
    strip = PixelStrip()
    effect = ColorEffect(strip, Colors.RED)
    effect.start()

    mqttClient = SimpleMqttClient("notreggsdf4323423", BROKER_ADDRESS)
    mqttClient.subscribe("some/other/random/topic", mqtt_message_handler)

    try:
        while True:
            effect.run()
            sleep(10)
    except KeyboardInterrupt:       # Catch CTRL-C
        mqttClient.stop()
        print ("Bye Bye")
        sys.exit()
