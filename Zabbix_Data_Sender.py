import syslog
import Adafruit_DHT
import os

### Enter the IP/Hostname of your Zabbix Server here ###

ip = 

### Enter the hostname of the Pi running the script here ###

hostname = 

pin = 17
key1 = 'Temp'
key2 = 'Hum'
x = 0
syslog.syslog('***** STARTING TEMP/HUMID GATHERING *****')
Sensor = Adafruit_DHT.AM2302
try:
    hum, tem = Adafruit_DHT.read_retry(Sensor, pin)
    syslog.syslog('***** GOT TEMP AND HUMID *****')
    tem_f = 1.8*float(tem) + 32
    syslog.syslog("***** TEMP={} HUMIDITY={} *****".format(tem_f,hum))
    print("Temp: {}".format(tem_f))
    print("Humidity: {}".format(hum))
    os.system('zabbix_sender -z 10.0.0.11 -s "M-RPIZ-01" -k {} -o {}'.format(ip,hostname,key1,float(tem_f)))
    os.system('zabbix_sender -z 10.0.0.11 -s "M-RPIZ-01" -k {} -o {}'.format(ip,hostname,key2, float(hum)))
    syslog.syslog('***** FINISHED TEMP/HUMID GATHERING *****')

except Exception as e:
    syslog.syslog('***** FAILED TO GET TEMP/HUMID BECAUSE: [{}] *****'.format(e))
    print(e)
    exit
