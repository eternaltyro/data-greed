#!/usr/bin/env python
# TODO: x axis labels to be turned vertical

from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import csv

timelist = []
valuelist = []

csvfile = 'electricity_usage.csv'
with open(csvfile) as csvhandle:
    usage = csv.reader(csvhandle, delimiter=',')
    for row in usage:
        timelist.append(datetime.strptime(row[0], "%Y-%B-%d %H:%M"))
        valuelist.append(row[1])
"""
fd = open(csvfile)
for i in csv.reader(fd)


"""
# Column parser for datetime
timeaxis = np.array(timelist)
valueaxis = np.array(valuelist)

plt.plot(timeaxis, valueaxis)
plt.savefig('elec_use.png', bbox_inches='tight')
plt.savefig('elec_use.svg')
plt.show()
