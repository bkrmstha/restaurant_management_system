from django.urls import path

from rms.views import category, category_detail, table, inventory

urlpatterns = [
    path('category/', category),
    path('category/<int:id>', category_detail),
    path('table/', table),
    path('inventory/', inventory)
]

