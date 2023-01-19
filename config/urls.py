from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', top, name='top'),
    path('', include('accounts.urls')),
    path('', include('lifemanage.urls')),
]
