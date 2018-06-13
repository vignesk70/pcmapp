from django import forms
from django.forms.models import inlineformset_factory
from .models import Member, Car, Payment




class NewMemberRegistrationForm(forms.ModelForm):
    #member_address_state = forms.ChoiceField(choices=STATE_CHOICES)
    class Meta:
        model = Member
        fields = ['member_name','member_email','member_phone','member_birthdate','member_address_state','member_address_postcode','member_on_chat','member_source']
        widgets = {
            'member_birthdate': forms.DateInput(attrs={'type': 'date', 'format' :'YYYY-MM-DD'}),
            'member_name' : forms.TextInput(attrs={'size':40}),
            'member_email' : forms.TextInput(attrs={'size':40}),
            'member_address_postcode' : forms.TextInput(attrs={'size':5}),
        }

class NewMemberCarRegistrationForm(forms.ModelForm):
    class Meta:
        model=Car
        fields = ['member_id','car_reg_no','car_model','car_engine_chasis']

CarRegistrationFormSet =  inlineformset_factory(Member,
    Car,
    fields = ['member_id','car_reg_no','car_model','car_engine_chasis','car_primary_sec'],
    extra=1)
PaymentFormSet = inlineformset_factory(Member,
    Payment,
    fields = ['payment_date','payment_amount','payment_type','payment_receipt_image'],
    extra=1,
    widgets = {'payment_date':forms.DateInput(attrs={'type': 'date', 'format' :'YYYY-MM-DD'})})

class SCCheckForm(forms.Form):
    car_reg_no = forms.CharField(label='Car Registration number', max_length=10)

    def clean_car_reg_no(self):
        car_reg_no = self.cleaned_data['car_reg_no']
        car_reg_no = car_reg_no.replace(" ","")
        try:
            obj = Car.objects.get(car_reg_no=car_reg_no)
            return car_reg_no
        except Car.DoesNotExist:
            raise forms.ValidationError('No record found')
