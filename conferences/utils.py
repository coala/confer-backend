import requests
from django.conf import settings
from django.contrib.admin.utils import quote


def get_geo(address):
    result = (None, None)
    if address.replace(',', '').strip():

        address = quote(address.lower().encode("utf-8"))
        sensor = "false"
        url = '{url}?address={address}&sensor={sensor}'.format(url=settings.GOOGLE_GEOCODE_ENDPOINT,
                                                               address=address,
                                                               sensor=sensor)

        response = requests.get(url)
        result = response.json()
        if result['status'] == 'OK':
            lat = str(result['results'][0]['geometry']['location']['lat'])
            lng = str(result['results'][0]['geometry']['location']['lng'])
            result = (lat, lng)

        else:
            result = (None, None)

    return result
