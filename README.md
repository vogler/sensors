# Log sensor data using RPi and ESP8266
Example: https://thingspeak.com/channels/321821

[Sensors](https://github.com/vogler/sensors) -> [MQTT](https://mosquitto.org/) -> [Telegraf](https://github.com/influxdata/telegraf) -> [InfluxDB](https://github.com/influxdata/influxdb) -> [Chronograf](https://github.com/influxdata/chronograf):
![Chronograf dashboard](https://i.imgur.com/KdjZi8j.png)

## Sensors
| Sensor    	| Measurement                                                         	| Interface   	| Host           	| Publish to           	|
|-----------	|---------------------------------------------------------------------	|-------------	|---------------	|----------------------	|
| [BME280](https://github.com/vogler/sensors/blob/master/thingspeak.py)    	| temperature (C), pressure (mBar), humidity (%)                      	| I2C         	| RPi3          	| thingspeak, MQTT 	|
| [TSL2561](https://github.com/vogler/sensors/blob/master/thingspeak.py)   	| visible light (lux), infrared, broadband                            	| I2C         	| RPi3          	| thingspeak, MQTT 	|
| [MH-Z19B](https://github.com/vogler/mh-z19)   	| CO2 (ppm)                                                           	| UART (USB)  	| RPi3          	| MQTT                 	|
| [PMS7003](https://github.com/vogler/python-pms7003)   	| particle matter (counts and PM [1, 2.5, 10] ug/m³)                  	| UART (pins) 	| RPi3          	| MQTT                 	|
| [FlowMeter](https://github.com/vogler/FlowMeter) 	| shower usage via Hall effect flow sensor (ml/s, total_ml, duration) 	| GPIO ISR    	| Wemos D1 mini 	| MQTT                 	|
| [BloodPressureWifi](https://github.com/vogler/BloodPressureWifi/tree/68fa73118bdff4fb1534a2af755457619081ecbf) 	| read Beurer blood pressure monitor (hiBP, loBP, HR)         	| SPI EEPROM    	| Wemos D1 mini 	| MQTT                 	|

[thingspeak.py](thingspeak.py) reads BME280 and TSL2561, the other sensors run as standalone services (see their repos).

## Setup

Install dependencies with `pipenv install`.
Register at www.thingspeak.com and replace `Config.key` in `thingspeak.py`.

Run with
~~~
./thingspeak.py 2>&1 | tee -a thingspeak.log
~~~
