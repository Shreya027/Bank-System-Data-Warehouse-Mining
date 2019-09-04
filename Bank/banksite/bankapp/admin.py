from django.contrib import admin
#from mysite.travel.models import Place
# Register your models here.


from .models import Account, Credit, Customer, Interest, Region, Csv


admin.site.register(Account)
admin.site.register(Credit)
admin.site.register(Customer)
admin.site.register(Interest)
admin.site.register(Region)
admin.site.register(Csv)


