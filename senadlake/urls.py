from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *

# admin.site.site_header = "Sena DataLake Admin"
# admin.site.site_title = "Sena DataLake Admin"
# admin.site.index_title = "Welcome To Sena DataLake Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loads.urls')),
    path('', include('raiting.urls')),
    path('', include('users.urls')),

    path('', home, name='home'),
    path('project', project, name='project'),

    path('privacy', privacy, name='privacy'),
    # path('page401', page401, name='page401'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 401 Unauthorized
# 403 Forbidden
# 404 Not Found