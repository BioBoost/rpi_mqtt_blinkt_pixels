# Raspberry Pi Zero W / 2 / 3 MQTT Blinkt Pixel Controller

Very simple MQTT client app in Python that allows control of Blinkt pixel strip
attached to my kids bed.

## Dependencies

```shell
pip3 install paho-mqtt
pip3 install jsonschema
pip3 install blinkt
```

## NeoPixels

You can make use of Jeremy Garffs neopixel lib for the Rpi. More info at:

* https://learn.adafruit.com/neopixels-on-raspberry-pi?view=all
* https://github.com/jgarff/rpi_ws281x

## Installing rpi_ws281x

```shell
sudo apt-get update
sudo apt-get install build-essential python3-dev git scons swig
cd ; git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python3 setup.py install
```

## Run as a Service

```shell
chmod +x app.py
sudo su
cp mqtt_pixels.service /etc/systemd/system
systemctl enable mqtt_pixels.service
systemctl start mqtt_pixels.service
```
