#!/usr/bin/python
# https://www.raspberrypi-spy.co.uk/2015/06/basic-temperature-logging-to-the-internet-with-raspberry-pi/
import time, os, sys
import urllib, urllib2

import bme280
from tsl2561.TSL2561 import TSL2561

tsl = TSL2561(0x39,"/dev/i2c-1")
tsl.enable_autogain()
tsl.set_time(0x00)

class Config:
  interval = 1
  url = 'https://api.thingspeak.com/update'
  key = 'ABCDEFGH12345678'


def sendData(url, key, temp, pres, humi, lux):
  values = { 'api_key': key, 'field1': temp, 'field2': pres, 'field3': humi, 'field4': lux }

  postdata = urllib.urlencode(values)
  req = urllib2.Request(url, postdata)

  log = time.strftime("%d-%m-%Y,%H:%M:%S") + ","
  log += "{:.2f}C".format(temp) + ","
  log += "{:.2f}mBar".format(pres) + ","
  log += "{:.2f}per".format(humi) + ","
  log += "%slux" % lux + ","

  try:
    response = urllib2.urlopen(req, None, 5)
    html_string = response.read()
    response.close()
    log += 'Update ' + html_string
  except urllib2.HTTPError, e:
    log += 'Server could not fulfill the request. Error code: ' + e.code
  except urllib2.URLError, e:
    log += 'Failed to reach server. Reason: ' + e.reason
  except Exception, e:
    log += type(e).__name__ + ': ' + e.message

  print log

def main():
  while True:
    temperature,pressure,humidity = bme280.readBME280All()
    sendData(Config.url, Config.key, temperature, pressure, humidity, tsl.lux())
    sys.stdout.flush()
    time.sleep(Config.interval*60)

if __name__=="__main__":
   main()
