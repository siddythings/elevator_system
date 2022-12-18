from django.contrib import admin
from .models import Elevator, Request, MaintenanceStatus

# Register your models here.
admin.site.register(Elevator)
admin.site.register(Request)
admin.site.register(MaintenanceStatus)
