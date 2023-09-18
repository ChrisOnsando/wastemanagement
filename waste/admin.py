from django.contrib import admin

from waste.models import Bin, Complaint

admin.site.register(Bin)
admin.site.register(Complaint)