import grequests
import requests
import random
import time

n = int(input('Requests - '))
i = 0
count = 0
y = 0
n_i = str(input('Need interval(y/n) - '))
ts = int(time.time())
strs = []

if n_i == 'y':
    rps = int(input('Rounds - '))
while i < n:
    i+=1
    ts += 1
    random.seed(ts)
    t = random.randint(10, 30)
    hm = random.uniform(20, 40)
    pr = random.randint(95345, 95375)
    t0 =  random.randint(80, 120)
    t1 =  random.randint(80, 120)
    t2 =  random.randint(80, 120)
    t3 =  random.randint(80, 120)
    t4 =  random.randint(80, 120)
    t5 =  random.randint(80, 120)
    t6 =  random.randint(80, 120)
    t7 =  random.randint(80, 120)
    t8 =  random.randint(80, 120)
    uext = random.uniform(3, 6)
    upow = random.uniform(3, 6)
    soil1 = random.randint(1314, 1514)
    soil2 = random.randint(1314, 1514)
    soil3 = random.randint(1314, 1514)
    id = str(random.randint(0, 80))
    id = id.zfill(4)
    ver = random.randint(1, 5)

    strs.append('{'+'"t": {0}, "hm": {1}, "pr": {2}, "t0": {3}, "t1": {4}, "t2": {5}, "t3": {6}, "t4": {7}, "t5": {8}, "t6": {9}, "t7": {10}, "t8": {11}, "Uext": {12}, "Upow": {13}, "soil1": {14}, "soil2": {15}, "soil3": {16}, "stationID": "{17}", "device_type": "Z", "firmware_version": {18}, "time": {19}'.format(t, hm, pr, t0, t1, t2, t3, t4, t5, t6, t7, t8, uext, upow, soil1, soil2, soil3, id, ver, ts)+'}')

rs = [grequests.post('https://en3hsl28r8kxbsa.m.pipedream.net', json=params) for params in strs]

if n_i == 'y':
    while y < rps:
        y+=1
        for r in grequests.imap(rs, size=16):
            count += 1
            print(count, 'done!')
        time.sleep(1)
else:
    for r in grequests.imap(rs, size=16):
        count += 1
        print(count, 'done!')
