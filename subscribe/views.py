from django.shortcuts import render
from subscribe.models import Subscribe, Company, Phone_number, Company_Phone_List
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth import get_user_model
from subscribe.serializers import SubscribeSerializer, CompanySerializer,Company_Phone_ListSerializer
from rest_framework import viewsets
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

User=get_user_model()


# All Users subscribe view by superuser
class AllUserViewset(viewsets.ModelViewSet):
	serializer_class = SubscribeSerializer
	queryset = Subscribe.objects.all()
	permission_classes=[IsAdminUser]

# Operation on login user
class SubscribeViewset(viewsets.ModelViewSet):
	serializer_class = SubscribeSerializer
	queryset = Subscribe.objects.all()
	permission_classes=[IsAuthenticated]
	
	def create(self, request, *args, **kwargs):
		data=request.data
		new_obj = Subscribe.objects.create(plan=data['plan'],
								    user=request.user)
		new_obj.save()
		serializer = SubscribeSerializer(new_obj)
		return Response(serializer.data)

	def list(self, request, *args, **kwargs):
		queryset = Subscribe.objects.get(id=request.user.id)
		serializer = SubscribeSerializer(queryset)
		return Response(serializer.data)

# company added by admin
class CompanyViewset(viewsets.ModelViewSet):
	serializer_class = CompanySerializer
	queryset = Company.objects.all()
	permission_classes=[IsAdminUser]

# This will add multiple phone numbers for specific company
class Company_Phone_ListViewset(viewsets.ModelViewSet):
	serializer_class = Company_Phone_ListSerializer
	queryset = Company_Phone_List.objects.all()
	permission_classes=[IsAdminUser]