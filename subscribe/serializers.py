from rest_framework import serializers
from subscribe.models import Subscribe, Company, Phone_number, Company_Phone_List

class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields= ['id','plan']

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = '__all__'
