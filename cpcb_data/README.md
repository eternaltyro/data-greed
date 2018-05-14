## Central Pollution Control Board - Data

This is an attempt to fetch / scrape / steal data from the [CPCB site](http://164.100.160.234:9000/).

In an ideal world, the data would be available in a consumable fashion
in CSV or JSON format. Unfortunately, I wasn't able to find such a feed.
Either that or it's not an ideal world! 

### Files
 - config.json - General stuff, legends, categorization and such
 - stations.json - All ze data monitoring stations listed
 - data JSON - The actual data for a particular day at a particular city over multiple time spans

### stations file

### data JSON
Available at the endpoint `/metrics/station/<station_id>` with parameters `d` in `DD/MM/YYYY` format and `h`. Dunno what `h` is at the moment. Station_id can be fetched from stations.json. An example URI: `/metrics/station/798?id=19%2F10%2F2017&h=23`

Data for a particular station includes metadata about the station
including name, operating status and date. Following that are metrics for major pollutants: 
- Sulphur dioxide (SO2)
- Nitrogen dioxide (NO2)
- Carbon monoxide (CO)
- Ozone (O3) and
- Fine Particulate Matter of 2.5 micrometers size (PM2.5)
