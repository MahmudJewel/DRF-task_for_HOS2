from django.shortcuts import render
from subscribe.models import Subscribe, Company, Phone_number, Company_Phone_List
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth import get_user_model
from subscribe.serializers import SubscribeSerializer
from rest_framework import viewsets
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

User=get_user_model()

# Create your views here.

# get, put and post order
class SubscribeViewset(viewsets.ModelViewSet):
	serializer_class = SubscribeSerializer
	queryset = Subscribe.objects.all()
	# permission_classes=[IsAuthenticated]
	
	def create(self, request, *args, **kwargs):
		data=request.data
		new_obj = Subscribe.objects.create(plan=data['plan'],
								    user=request.user)
		new_obj.save()
		serializer = SubscribeSerializer(new_obj)
		return Response(serializer.data)