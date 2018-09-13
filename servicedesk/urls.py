from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('engineer/', include('engineer.urls')),
    path('supervisor/', include('supervisor.urls')),
    path('admin/', admin.site.urls),
]