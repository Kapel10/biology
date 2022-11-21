from django.contrib import admin
from .models import Diseasetype,Country,Disease,Discover,Users,Publicservant,Doctor,Specialize,Record
# Register your models here.

admin.site.register(Diseasetype)
admin.site.register(Country)
admin.site.register(Disease)
admin.site.register(Discover)
admin.site.register(Users)
admin.site.register(Publicservant)
admin.site.register(Doctor)

admin.site.register(Specialize)
admin.site.register(Record)