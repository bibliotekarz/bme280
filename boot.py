try:
    import gc
import time

import esp

import BME280
import network
import usocket as socket
import webrepl
from machine import I2C, Pin

except:
import socket
import gc
import network
import time
import esp
from machine import Pin, I2C
import BME280

network.WLAN(network.AP_IF).active(False)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.config(dhcp_hostname="termometr")
sta_if.connect('dino', 'Krol')
count = 0

while not sta_if.isconnected():
    time.sleep_ms(1)
    count += 1
    if count == 10000:
        print('Not connected')
        break
print('Config: ', sta_if.ifconfig())

esp.osdebug(None)
gc.collect()
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)

webrepl.start()
