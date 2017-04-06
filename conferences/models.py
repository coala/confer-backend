# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from .utils import get_geo


class Tag(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Conference(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    source_url = models.CharField(max_length=512, null=True, blank=True)
    website = models.CharField(max_length=512, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    cfp_closes = models.DateTimeField(null=True, blank=True)
    finaid_closes = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    place = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    postcode = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    geo_lat = models.DecimalField('latitude', max_digits=13, decimal_places=10, blank=True, null=True)
    geo_long = models.DecimalField('longitude', max_digits=13, decimal_places=10, blank=True, null=True)

    def __str__(self):
        return self.name

    def update_coordinate(self, address=None):
        if address:
            latitude, longitude = get_geo(address)
        else:
            latitude, longitude = get_geo("%s, %s, %s, %s" % (self.address, self.postcode, self.city, self.country))
        if latitude and longitude:
            self.geo_lat = latitude
            self.geo_long = longitude
            self.save()
