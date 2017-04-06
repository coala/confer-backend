# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Conference, Tag

admin.site.register(Tag)
admin.site.register(Conference)
