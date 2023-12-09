from django.urls import path
from django.contrib import admin

from principal.views import load_data, home

# Add your URLs here.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('load/', load_data, name='load_data'),
    path('home/', home, name='home')
]