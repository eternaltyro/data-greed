Electricity Usage

This directory contains my attempts to map my electricity usage over a time
period. I'm trying to track my usage everyday. Electricity values are units of
usage. Each unit equals to 1-kWh (rate of energy consumption)

The readings are taken in the electricity consumption meter twice every day if
possible. 

Appliances: 
-----------
1 x 1975W airconditioner
2 x 15W CFL lamps
1 x ~70W Ceiling fan 
1 x 36W CFL Tube lamp

Time:
----
Ceiling Fan - 8-10 hr / day ~ 120-150 Wh / day
AC - 1-3 hr / day           ~ 2-6 kWh / day
CFL lamps - 1-2 hr / day    ~ 70-140 Wh / day
Tube lamp - 2-5 hr / day    ~ 72-180 Wh / day

Estimated Monthly usage - Min 62 kWh, Max 191 kWh

- Data Logging is done manually to a CSV file
- Use euparser.py file to plot the data
- Time format is "%Y-%B-%d %H:%M"

TODO:
====
- Make histogram overlay
- Make the x-axis labels better
