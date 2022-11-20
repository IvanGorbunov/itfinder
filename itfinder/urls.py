from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
] + doc_url
