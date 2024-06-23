from django.contrib import admin
from django.urls import path, include

from api.views import index

# add urls from api
from api import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    
    path('api/v1/', include(api_urls))
]
