
from django.urls import path , include

urlpatterns = [
    path('api/', include('api.urls')),
    path('home/', include('home.urls')),
]