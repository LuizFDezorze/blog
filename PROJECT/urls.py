from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('APP.urls')),
    path('MEMBERS/', include('django.contrib.auth.urls')),
    path('MEMBERS/', include('MEMBERS.urls')),
]
