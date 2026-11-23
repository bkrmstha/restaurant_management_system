from django.urls import path

from rms.views import category

urlpatterns = [
    path('category/', category),
]
