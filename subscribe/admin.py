from django.contrib import admin
from subscribe.models import Subscribe, Company, Phone_number, Company_Phone_List
# Register your models here.
lst = [Subscribe, Company, Phone_number, Company_Phone_List]
admin.site.register(lst)
