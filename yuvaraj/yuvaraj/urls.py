from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('yuvi.urls')),
    path('admin/', admin.site.urls),
]