from django.contrib import admin
from django.urls import path, include

from api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include(urls))   
]
