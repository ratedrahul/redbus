from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Route)
admin.site.register(Stop)
admin.site.register(Bus)