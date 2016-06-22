import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig, ax = plt.subplots(1)
timelist = [0,5,9,10,15]
valuelist = [0,1,2,3,4]


# Logic that populates timelist and valuelist

timeaxis = np.array(timelist)
valueaxis = np.array(valuelist)
ax.plot(timeaxis, valueaxis, 'r-')

# rotate and align the tick labels so they look better
fig.autofmt_xdate()

# use a more precise date string for the x axis locations in the
# toolbar
import matplotlib.dates as mdates
ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
plt.savefig('elec_use.png', bbox_inches='tight')
plt.show()

