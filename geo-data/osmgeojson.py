#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program to upload GeoJSON based data to Open Street Map
"""
from geojson import Point
from geojson import Feature, FeatureCollection
from geojson import dump, load
from osmapi import OsmApi
import os

DATAFILE='libraries_new.geojson'
TESTFILE='libraries_test.geojson'
GEODATAFILE=DATAFILE # Switch between test data and actual data
# COORD_SYSTEM='degree'
COORD_SYSTEM='decimal'

def degree_decimal(dms_list):
    return dms_list[0] + (dms_list[1] / 60.0) + (dms_list[2] / 3600.0)

if COORD_SYSTEM == 'decimal':
    lat = input('lat: ')
    lon = input('lon: ')
elif COORD_SYSTEM == 'degree':
    lat_dms = input('deg,min,sec: ')
    lon_dms = input('deg,min,sec: ')
    lat = degree_decimal([float(x.strip()) for x in lat_dms.split(',')])
    lon = degree_decimal([float(y.strip()) for y in lon_dms.split(',')])

def prompt():
    print("Select Option")
    print("0. Exit")
    print("1. Add a node")
    print("2. Get node(s)")

def add_to_osm():
    connection = OsmApi(passwordfile=u'', api=OSM_EP)

# GeoJSON point is (Easting, Northing) / (Long, Lat) order!
_point = Point((float(lon.strip()),float(lat.strip())))

''' Properties: {
        Name: Name of the library
        Operator: Directorate of Public Libraries
        Opening Hours: Open hours in OSM format
        Address: Door number if available and street
'''

name = input('Name: ')
timings = input('Time: ')
street = input('Street: ')
housenumber = input('Door: ')
postcode = input('PINCODE: ')

_feature = Feature(geometry=_point, properties={
    'amenity':'library',
    'name':name,
    'operator':'Directorate of Public Libraries',
    'opening_hours':timings,
    'addr:country':'IN',
    'addr:city':'Chennai',
    'addr:street':street,
    'addr:housenumber':housenumber,
    'addr:postcode':postcode,
    'marker-color': '#00ff00',
    'marker-symbol': 'library'
    } )

FILE_EMPTY = True if os.stat(GEODATAFILE).st_size == 0 else False

if not FILE_EMPTY:
    with open(GEODATAFILE,'r') as _data:
        current = load(_data)
        _featureCollection = current['features']
        _featureCollection.append(_feature)
        print("Total libraries: %d" % len(_featureCollection))
        libraries = FeatureCollection(_featureCollection)
else:
    libraries = FeatureCollection([_feature])

# Write data to file
with open(GEODATAFILE,'w+') as data:
    dump(libraries, data, indent=4, sort_keys=True)


