"""transition URL Configuration"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('profile/', include("backend.profiles.urls")),
    path('', include("backend.public.urls")),

]
# к урл добавим файл документации
urlpatterns +=doc_urls

# подключили медиа и статик
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)