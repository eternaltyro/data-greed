import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig, ax = plt.subplots(1)
timelist = [0,5,9,10,15]
valuelist = [0,1,2,3,4]

guassian_numbers = np.random.normal(size=10000)
# Logic that populates timelist and valuelist

timeaxis = np.array(timelist)
valueaxis = np.array(valuelist)
print guassian_numbers
plt.hist(guassian_numbers, bins=150)
plt.show()

