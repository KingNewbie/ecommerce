from django.urls import path

from products.api.views.general_views import MeasureUnitListAPIView,IndicatorListAPIView,CategoryProductListAPIView
from products.api.views.product_views import (
    ProductListCreateAPIView,ProductRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('measure_unit/',MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/',IndicatorListAPIView.as_view(), name = 'indicator'),    
]