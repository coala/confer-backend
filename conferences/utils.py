import requests
from django.contrib.admin.utils import quote


def get_geo(address):
    result = (None, None)
    if address.replace(',', '').strip():

        address = quote(address.lower().encode("utf-8"))
        sensor = "false"
        url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=%s" % (address, sensor)

        response = requests.get(url)
        result = response.json()
        if result['status'] == 'OK':
            lat = str(result['results'][0]['geometry']['location']['lat'])
            lng = str(result['results'][0]['geometry']['location']['lng'])
            result = (lat, lng)

        else:
            result = (None, None)

    return result
