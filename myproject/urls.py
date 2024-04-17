
from django.contrib import admin
from django.urls import path
from .views import homepage, aboutpage

urlpatterns = [
    path('', homepage),
    path('about/',aboutpage),
    path("admin/", admin.site.urls),
]
