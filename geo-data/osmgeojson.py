#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program to upload GeoJSON based data to Open Street Map
"""
from geojson import Point
from geojson import Feature, FeatureCollection
from geojson import dump, load
from prompt_toolkit.shortcuts import input_dialog

from constants import *
import os


class Amenity(object):

    def __init__(self, city, country, doornumber, lat, lon, postcode, street):
        self.city = city
        self.country = country
        self.doornumber = doornumber
        self.latitude = lat
        self.longitude = lon
        self.postcode = postcode
        self.street = street

    def get_coord(self):
        if not isinstance(self.latitude, float):
            self.latitude = float(self.latitude.strip())

        if not isinstance(self.longitude, float):
            self.longitude = float(self.longitude.strip())

        _point = Point((self.longitude, self.latitude))
        return _point

    def make_address(self):
        _address = {
            'addr:country': self.country,
            'addr:city': self.city,
            'addr:street': self.street,
            'addr:doornumber': self.doornumber,
            'addr:postcode': self.postcode
        }

        return _address


class Library(Amenity):

    def __init__(self, city, country, doornumber, lat, lon, postcode, street,
                 name, opening_hours, amenity='Library',
                 marker_colour='#00ff00', marker_symbol='library',
                 operator='Directorate of public libraries'):

        super().__init__(city, country, doornumber, lat, lon, postcode, street)

        self.amenity = amenity
        self.name = name
        self.operator = operator
        self.opening_hours = opening_hours
        self.marker_colour = marker_colour
        self.marker_symbol = marker_symbol

    def make_feature(self):

        point = self.get_coord()

        _attributes = {
            'amenity': self.amenity,
            'name': self.name,
            'operator': self.operator,
            'opening_hours': self.opening_hours,
            'marker-color': self.marker_colour,
            'marker-symbol': self.marker_symbol
        }

        _attributes.update(self.make_address())

        _feature = Feature(geometry=point, properties=_attributes)
        return _feature


def main():
    lat = input_dialog(title='Latitude', text='Type latitude of library')
    lon = input_dialog(title='Longitude', text='Type longitude of library')
    city = input_dialog(title='Library City',
                        text='Which city is the library in?')
    street = input_dialog(title='Address:Street', text='Street Name')
    doornumber = input_dialog(title='Address:Doornumber', text='Door number')
    postcode = input_dialog(title='Address:Postcode', text='PIN/Postcode')
    name = input_dialog(title='Library Name',
                        text='What is the name of the library?')
    opening_hours = input_dialog(title='Library Timings',
                                 text='What are the library timings?')

    _library = Library(
        name=name,
        lat=lat,
        lon=lon,
        opening_hours=opening_hours,
        city=city,
        street=street,
        doornumber=doornumber,
        postcode=postcode,
        country='IN'
    )

    _feature = _library.make_feature()

    FILE_EMPTY = True if os.stat(GEODATAFILE).st_size == 0 else False

    if not FILE_EMPTY:
        with open(GEODATAFILE, 'r') as _data:
            current = load(_data)
            _featureCollection = current['features']
            _featureCollection.append(_feature)
            print("Total libraries: %d" % len(_featureCollection))
            libraries = FeatureCollection(_featureCollection)
    else:
        libraries = FeatureCollection([_feature])

    # Write data to file
    with open(GEODATAFILE, 'w+') as data:
        dump(libraries, data, indent=4, sort_keys=True)


if __name__ == '__main__':
    main()
