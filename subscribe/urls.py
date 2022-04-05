from django.urls import path, include
from subscribe.views import SubscribeViewset,CompanyViewset,Company_Phone_ListViewset

# router 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subscribe', SubscribeViewset, basename='subscribe')
router.register('company', CompanyViewset, basename='company')
router.register('company-phone', Company_Phone_ListViewset, basename='company-phone')

urlpatterns = [
    path('', include(router.urls))
]