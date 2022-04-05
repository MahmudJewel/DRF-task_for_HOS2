from django.urls import path, include
from subscribe.views import SubscribeViewset

# router 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subscribe', SubscribeViewset, basename='subscribe')

urlpatterns = [
    path('', include(router.urls))
]