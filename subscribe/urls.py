from django.urls import path, include
from subscribe.views import SubscribeViewset,CompanyViewset

# router 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subscribe', SubscribeViewset, basename='subscribe')
router.register('company', CompanyViewset, basename='company')

urlpatterns = [
    path('', include(router.urls))
]