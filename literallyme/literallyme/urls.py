from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from mainapp.views import *
from literallyme import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('mainapp.urls')),
    path('', include('authentication.urls'))
]

# only for local server
if settings.DEBUG:
    # for django debug toolbar
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
