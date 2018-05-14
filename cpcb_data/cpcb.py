# -*- coding: utf-8 -*-
import datettime
import json
import requests

url = 'http://164.100.160.234:9000'
data_endpoint = '/metrics/station/{}'
today = datetime.date.today()

_ = requests.get(url + '/stations')
_ = json.loads(_.content.decode(_.encoding))
stations = []
def get_stations(url=stations_endpoint):
    requests.get(url.format(


