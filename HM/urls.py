"""
HM URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('firehub/', include('firehub.urls')),
    path('sudokusource/', include('sudokusource.urls'))
]
