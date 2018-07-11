from django.urls import path

from . import views

urlpatterns = [
    path('all_deals', views.AllDealsList.as_view(), name='index'),
    path('purchase', views.MakePurchase.as_view(), name='make purchase')
]