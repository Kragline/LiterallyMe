from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from mainapp.views import *
from literallyme import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('mainapp.urls'))
]

# only for local server
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
