#!/usr/bin/env python
# TODO: x axis labels to be turned vertical
# TODO: Actual usage rate as opposed to increasing trend

from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import csv

timelist = []
valuelist = []
oldreading = 0.00
newreading = 0.00
actual = []

csvfile = 'electricity_usage.csv'
with open(csvfile) as csvhandle:
    usage = csv.reader(csvhandle, delimiter=',')
    for row in usage:
        timelist.append(datetime.strptime(row[0], "%Y-%B-%d %H:%M"))
        valuelist.append(row[1])
        oldreading = newreading
        newreading = row[1]
#        actual.append(newreading-oldreading)

# Column parser for datetime
timeaxis = np.array(timelist)
valueaxis = np.array(valuelist)

plt.title('Electricity usage over time')
plt.xlabel('time')
plt.ylabel('reading')
plt.grid(True)
plt.plot(timeaxis, valueaxis, 'r-')
plt.savefig('elec_use.png', bbox_inches='tight')
plt.savefig('elec_use.svg')
plt.show()
