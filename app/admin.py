from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Patient)
admin.site.register(Staff)
admin.site.register(Room)
admin.site.register(Billing)
admin.site.register(RoomOccupancies)
admin.site.register(Medication)
