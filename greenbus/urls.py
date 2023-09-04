from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('buses.urls')),
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')),
    path('buses/', include('buses.urls')),
]
