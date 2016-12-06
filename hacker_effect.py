import time
import random

f = open('lores.txt', 'r')
read_data = f.read()
for ch in read_data:
        waittime = random.uniform(0, 0.175)
        time.sleep(waittime)
        print(ch, sep=' ', end='', flush=True)
print(" ")

