from django.urls import path

from rms.views import category, table, inventory

urlpatterns = [
    path('category/', category),
    path('table/', table),
    path('inventory/', inventory)
]

