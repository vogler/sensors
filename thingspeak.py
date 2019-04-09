#!/usr/bin/python
# https://www.raspberrypi-spy.co.uk/2015/06/basic-temperature-logging-to-the-internet-with-raspberry-pi/
import time, os, sys
import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse

import bme280
from tsl2561 import TSL2561, TSL2561_GAIN_16X

tsl = TSL2561(gain=TSL2561_GAIN_16X, autogain=True)

import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("localhost")
client.loop_start()
import json

class Config:
  interval = 10
  url = 'https://api.thingspeak.com/update'
  key = 'ABCDEFGH12345678'


def postThingspeak(temp, pres, humi, lux, bb, ir):
  values = { 'api_key': Config.key, 'field1': temp, 'field2': pres, 'field3': humi, 'field4': lux, 'field5': bb, 'field6': ir }

  postdata = urllib.parse.urlencode(values)
  req = urllib.request.Request(Config.url, postdata)

  log = time.strftime("%d-%m-%Y,%H:%M:%S") + ","
  log += "{:.2f}C".format(temp) + ","
  log += "{:.2f}mBar".format(pres) + ","
  log += "{:.2f}per".format(humi) + ","
  log += "%slux" % lux + ","
  log += "%sbb" % bb + ","
  log += "%sir" % ir + ","

  try:
    response = urllib.request.urlopen(req, None, 5)
    html_string = response.read()
    response.close()
    log += 'Update ' + html_string
  except urllib.error.HTTPError as e:
    log += 'Server could not fulfill the request. Error code: ' + str(e.code)
  except urllib.error.URLError as e:
    log += 'Failed to reach server. Reason: ' + str(e.reason)
  except Exception as e:
    log += type(e).__name__ + ': ' + e.message

  print(log)
  sys.stdout.flush()

def main():
  i = 1
  while True:
    temp,pres,humi = bme280.readBME280All()
    r_bme280 = { 'temperature': temp, 'pressure': pres, 'humidity': humi }

    bb, ir = tsl._get_luminosity()
    lux = tsl._calculate_lux(bb, ir)
    r_tsl2561 = { 'lux': lux, 'broadband': bb, 'infrared': ir }

    # mqtt
    client.publish("sensors/bme280", json.dumps(r_bme280))
    client.publish("sensors/tsl2561", json.dumps(r_tsl2561))

    if i == 6:
        postThingspeak(temp, pres, humi, lux, bb, ir)
        i = 1
    else:
        i += 1

    time.sleep(Config.interval)


if __name__=="__main__":
   main()
