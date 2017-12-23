import paho.mqtt.client as mqtt

class SimpleMqttClient(object):
    """A very simple MQTT client"""

    def __init__(self, uniqueId, server="broker.hivemq.com", port=1883):
        self.client = mqtt.Client(uniqueId)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(server, port, 60)
        self.start()

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
        else:
            print("Connection to broker failed with result code " + str(rc))

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print("No message callback registered for: " + msg.topic + " " + str(msg.payload))

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.disconnect()
        self.client.loop_stop(force=False)

    def subscribe(self, topic, callback=None):
        if callback != None:
            self.client.message_callback_add(topic, callback)
        self.client.subscribe(topic)

    def publish(self, topic, payload, QOS, doRetain=False):
        (status, mid) = self.client.publish(topic, payload, QOS, doRetain)
        return (status, mid)
