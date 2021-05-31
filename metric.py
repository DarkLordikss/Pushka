import requests
import time
from datetime import datetime

i = 0

while i == 0:
    start_time = datetime.now()

    requests.post('https://somnoynadno.ru/controller/send_data', data='{"t": 22, "hm": 29.5284, "pr": 95355, "t0": 103, "t1": 103, "t2": 103, "t3": 103, "t4": 103, "t5": 103, "t6": 103, "t7": 103, "t8": 103, "Uext": 4.476, "Upow": 4.152, "soil1": 1414, "soil2": 1468, "soil3": 1451, "stationID": "0080", "device_type": "Z", "firmware_version": 5, "time": 1622299862}')

    print('---', datetime.now() - start_time, '---', '\n')

    time.sleep(1)
