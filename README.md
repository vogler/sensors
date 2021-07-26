# Log sensor data using RPi and ESP8266
Example: https://thingspeak.com/channels/321821

[Sensors](https://github.com/vogler/sensors) -> [MQTT](https://mosquitto.org/) -> [Telegraf](https://github.com/influxdata/telegraf) -> [InfluxDB](https://github.com/influxdata/influxdb) -> [Chronograf](https://github.com/influxdata/chronograf):
![Chronograf dashboard](https://i.imgur.com/KdjZi8j.png)

## Sensors
| Sensor    	| Measurement                                                         	| Interface   	| Host           	| Publish to           	|
|-----------	|---------------------------------------------------------------------	|-------------	|---------------	|----------------------	|
| BME280    	| temperature (C), pressure (mBar), humidity (%)                      	| I2C         	| RPi3          	| thingspeak, MQTT 	|
| TSL2561   	| visible light (lux), infrared, broadband                            	| I2C         	| RPi3          	| thingspeak, MQTT 	|
| MH-Z19B   	| CO2 (ppm)                                                           	| UART (USB)  	| RPi3          	| MQTT                 	|
| PMS7003   	| particle matter (counts and PM [1, 2.5, 10] ug/m³)                  	| UART (pins) 	| RPi3          	| MQTT                 	|
| FlowMeter 	| shower usage via Hall effect flow sensor (ml/s, total_ml, duration) 	| GPIO ISR    	| Wemos D1 mini 	| MQTT                 	|
| BloodPressureWifi 	| read Beurer blood pressure monitor (hiBP, loBP, HR)         	| SPI EEPROM    	| Wemos D1 mini 	| MQTT                 	|

[thingspeak.py](thingspeak.py) only reads BME280 and TSL2561. The other sensors run as standalone services (see their repos).

## Setup

Install dependencies with `pipenv install`.
Register at www.thingspeak.com and replace `Config.key` in `thingspeak.py`.

Run with
~~~
./thingspeak.py 2>&1 | tee -a thingspeak.log
~~~
