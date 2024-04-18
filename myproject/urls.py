
from django.contrib import admin
from django.urls import path
from .views import homepage, aboutpage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage),
    path('about/',aboutpage),
    path("admin/", admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
