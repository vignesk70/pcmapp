from django.contrib import admin
from django.contrib.admin import AdminSite

# Register your models here.
from .models import Member,Car,Payment

class PCMAdminSite(AdminSite):
    site_header = 'Peugeot Club Administration'

class PaymentInLine(admin.TabularInline):
    model = Payment
    choices = 1

class CarInLine(admin.TabularInline):
    model = Car
    choices =1

class MemberAdmin(admin.ModelAdmin):
    #fields = ['member_name','member_expiry_date']
    search_fields = ['member_name']
    list_display = ('member_name','member_expiry_date','member_phone',)
    inlines = [CarInLine,PaymentInLine]

#class CarAdmin(admin.ModelAdmin):
#    #list_display = ('car_reg_no')
#    search_fields = ['car_reg_no']
#    inlines = [PaymentInLine]

admin_site = PCMAdminSite(name='pcmadmin')
admin_site.register(Member,MemberAdmin)


