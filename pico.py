from machine import ADC
import time

def alert():
    print('Alert!!!')

while True:
    sensor = ADC(4)    
    vol = sensor.read_u16() * (3.3/65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print('temperature:', temperature)
    if temperature > 24:
        alert()
    time.sleep(60)

