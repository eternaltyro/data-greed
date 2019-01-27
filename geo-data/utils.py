#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from constants import *
from osmapi import OsmApi


def degree_decimal(dms_list):
    """Compute decimal coordinates from list [degree, minute, second]

    Args:
        list

    Returns:
        float
    """
    return dms_list[0] + (dms_list[1] / 60.0) + (dms_list[2] / 3600.0)


def prompt():
    print("Select Option")
    print("0. Exit")
    print("1. Add a node")
    print("2. Get node(s)")


def add_to_osm():  # Dummy function
    connection = OsmApi(passwordfile=u'', api=OSM_EP)
    return connection


def get_decimal(lat_dms: str, lon_dms: str) -> tuple:
    """Convert degree, minute, second format to decimal format

    Args:
        lat_dms: A string for latitude in degree,minute,second format
        lon_dms: A string for longitude in degree,minute,second format

    Returns:
        tuple: (lat decimal, lon decimal)

    """
    try:
        lat = degree_decimal([float(x.strip()) for x in lat_dms.split(',')])
        lon = degree_decimal([float(y.strip()) for y in lon_dms.split(',')])
    except Exception:
        raise

    return (lat, lon)
