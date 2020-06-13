from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from mptt_practice.models import Mptt_file

admin.site.register(Mptt_file, DraggableMPTTAdmin)
