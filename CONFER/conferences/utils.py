import json
import urllib
import urllib2


def get_geo(address):
    result = (None, None)
    if address.replace(',', '').strip():

        address = urllib.quote(address.lower().encode("utf-8"))
        sensor = "false"
        url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=%s" % (address, sensor)

        response = urllib2.urlopen(url).read()
        result = json.loads(response)
        if result['status'] == 'OK':
            lat = str(result['results'][0]['geometry']['location']['lat'])
            lng = str(result['results'][0]['geometry']['location']['lng'])
            result = (lat, lng)

        else:
            result = (None, None)

    return result
