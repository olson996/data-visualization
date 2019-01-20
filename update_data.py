#!/usr/bin/env python
import time
from random import *

openfile = open('samplefile.txt', 'r')
r = openfile.read()
r = r.split('\n')
if r[-1] == '':
	last_num = r[-2]
else:
	last_num = r[-1]
last_num = last_num.split(',')
i = int(last_num[0])
value = float(last_num[1])
openfile.close()

for x in range(i+1,i+20):
	data = open('samplefile.txt', 'a')
	index = str(x)
	value = round(value*uniform(0.7, 1.3), 2)
	y = index + ',' + str(value) + '\n'
	data.write(y)
	data.close()
	time.sleep(1)
