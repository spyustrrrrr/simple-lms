"""
URL Configuration untuk Simple LMS
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Tambahkan URL apps di sini (modul berikutnya):
    # path('api/courses/', include('courses.urls')),
    # path('api/users/', include('users.urls')),
]

# Serve media files saat development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
