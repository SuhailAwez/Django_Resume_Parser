from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from parser_app.views import upload_resume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_resume, name='upload_resume'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
