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

class PhoneSerializer(serializers.ModelSerializer):
	class Meta:
		model = Phone_number
		fields = '__all__'

class Company_Phone_ListSerializer(serializers.ModelSerializer):
	phone = PhoneSerializer()

	class Meta:
		model = Company_Phone_List
		fields = ['name', 'phone']
    
    # create is ovewritten as it has complex relationships 
	def create(self, validated_data):
		phone = validated_data.pop('phone')
		phone_obj = Phone_number.objects.create(**phone)
		company_phone = Company_Phone_List.objects.create(phone=phone_obj, **validated_data)
		return company_phone
