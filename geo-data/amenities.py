# !/usr/bin/env python
# 
# vim: set expandtab:tw=4:ts=4:sw=4:
# 
# This python program attempts to interactively collect user-provided
# information for OpenStreetMap amenities and upload them to OpenStreetMap
# Servers. 
#
# Requires OsmApi: `pip install osmapi` 
# Requires click: `pip install click`

from osmapi import OsmApi
import geojson
import click

class Amenity(object):
    def __init__(self, city, door, lat, lon, name, opening_hours, postcode, street):
       self._city = city
       self._door = door
       self._lat = lat
       self._lon = lon
       self._name = name
       self._opening_hours = opening_hours
       self._postcode = postcode
       self._street = street
       self._data = {
               u'lat': self._lat,
               u'lon': self._lon,
               u'tags': {
                  u'amenity': u'atm',
                  u'name': self._name,
                  u'operator': self.operator,
                  u'cash_in': self.cash_in,
                  u'fee': self.fee,
                  u'opening_hours': self._opening_hours,
                  u'postcode': self._postcode,
                  u'addr:city': self._city,
                  u'addr:street': self._street }
             }

    def atm(self, operator, cash_in='no', fee='some'):
        self.cash_in = cash_in
        self.fee = fee
        self.operator = operator
        data = {
                u'lat': self._lat,
                u'lon': self._lon,
                u'tags': {
                   u'amenity': u'atm',
                   u'name': self._name,
                   u'operator': self.operator,
                   u'cash_in': self.cash_in,
                   u'fee': self.fee,
                   u'opening_hours': self._opening_hours,
                   u'postcode': self._postcode,
                   u'addr:city': self._city,
                   u'addr:street': self._street }
              }
        return data

    def library(self, operator):
        self.operator = operator
        return {
            u'lat': self._lat,
            u'lon': self._lon,
            u'tags': {
                u'amenity': u'library',
                u'name': self._name,
                u'operator': self.operator,
                u'level': 1,
                u'opening_hours': self._opening_hours,
                u'postcode': self._postcode,
                u'addr:city': self._city,
                u'addr:street': self._street,
                u'addr:door': self._door }
            }

    def police(self, operator, phone, website):
        self.operator = operator
        self.phone = phone
        self.website = website
        return {
            u'lat': self._lat,
            u'lon': self._lon,
            u'tags': {
                u'amenity': u'police',
                u'name': self._name,
                u'operator': self.operator,
                u'opening_hours': self._opening_hours,
                u'phone': self.phone,
                u'website': self.website,
                u'postcode': self._postcode,
                u'addr:city': self._city,
                u'addr:street': self._street,
                u'addr:door': self._door }
            }


def putdata():
    if amenity == 'atm':
        atm()
    elif amenity == 'library':
        library()
    elif amenity == 'police':
        police()
    else:
        print ("Invalid Entry! Exiting..")
        raise SystemExit

def next_amenity(amenity_geojson):
    for amenity in amenity_geojson.get("features"):
        yield amenity

def upload_geojson(datafile):
    """ This function attempts to parse an existing geojson
    file and create an upload-able simple JSON that can be
    fed to the upload script
    """
    geo_file = open(datafile)
    geo_data = geojson.load(geo_file)

    for amenity in next_amenity(geo_data):
        coords = amenity["geometry"]["coordinates"]
    tags = amenity["properties"]
    del tags["marker-color"]
    del tags["marker-symbol"]
    data = {
        u'lat': coords[1],
        u'lon': coords[0],
        u'tag': tags
    }
    # print data _or_ upload data


@click.command()
@click.option('--endpoint', default='dev', type=click.Choice(['dev', 'live']),
    help='API endpoint; defaults to the dev endpoint')
@click.option('--amenity', default='library',
    type=click.Choice(['atm', 'library', 'police']),
    help='Amenity type. Supported: atm, library (default), police')
@click.option('--passwordfile', default='./.osm/creds',
    help='location of the password file. default: ./.osm/creds')
@click.option('--comment', default='Automated Upload',
    help='A reasonably short, useful changeset comment')
def greet(amenity, endpoint, passwordfile, comment):
    """ This program connects to the OSM API and creats a
        changeset, runs the function that populates and uploads
        the data to OSM and once that is done, closes the
        changeset

        Requires OsmApi: `pip install OsmApi`
    """
    if endpoint == 'dev':
        endpoint = "api06.dev.openstreetmap.org"
    elif endpoint == 'live':
        endpoint = "api.openstreetmap.org"
    #api_handle = OsmApi(passwordfile=passwordfile, api=endpoint)
    #changeset = api_handle.ChangesetCreate({u'comment': comment}) 
    lat = input('lat: ')
    lon = input('lon: ')
    name = raw_input('Name: ')
    time = raw_input('Time: ')
    postcode = raw_input('PINCODE: ')
    street = raw_input('Street: ')
    city = raw_input('City: ')
    door = raw_input('Numb: ')
    newSet = Amenity(city=city, door=door, lat=lat, lon=lon, name=name, opening_hours=time, postcode=postcode, street=street)
    if amenity == 'atm':
        dat = newSet.atm('Bank')
        print dat
    elif amenity == 'library':
        dat = newSet.library('Libr')
        print dat
    elif amenity == 'police':
        dat = newSet.police('Police', '9823492', 'ntoe.com')
        print dat
    # Call the upload function or have data function call upload function
    #api_handle.flush()
    #api_handle.ChangesetClose()

if __name__ == '__main__':
    greet()
