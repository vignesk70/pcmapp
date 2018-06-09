from django.db import models
from datetime import date
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    STATE_CHOICES = (
        ('JH','Johor'),
        ('KH','Kedah'),
        ('KN','Kelantan'),
        ('KL','Kuala Lumpur'),
        ('LA','Labuan'),
        ('ME','Melaka'),
        ('NS','Negeri Sembilan'),
        ('PH','Pahang'),
        ('PK','Perak'),
        ('PL','Perlis'),
        ('PG','Pulau Pinang'),
        ('PJ','Putrajaya'),
        ('SA','Sabah'),
        ('SK','Sarawak'),
        ('SL','Selangor'),
        ('TE','Terengganu'),
    )
    SOURCE_CHOICES = (
        ('FB','Facebook'),
        ('TW','Twitter'),
        ('SC','Service Center'),
        ('IN','Instagram'),
        ('RE','Referral'),
        ('WO','Word of Mouth'),
        ('OT','Other'),
        )

    member_name = models.CharField(max_length=200, verbose_name='Full Name')
    member_email = models.EmailField(max_length=200, verbose_name='Email Address')
    member_phone = models.CharField(max_length=20,verbose_name='Mobile Number')
    member_since = models.DateField(blank=True, null=True)
    member_birthdate = models.DateField(blank=True, null=True, verbose_name='Your Birthdate')
    member_address_state = models.CharField(max_length=2,choices=STATE_CHOICES,blank=True,null=True, verbose_name='Current Location (State)')
    member_address_postcode = models.CharField(max_length=5,blank=True,null=True, verbose_name = 'Postcode')
    member_on_chat = models.BooleanField(default=True,verbose_name = 'Would you like to be added to our WhatsApp Group?' )
    member_source = models.CharField(max_length=2,choices = SOURCE_CHOICES,blank=True,null=True,verbose_name = 'Where did you hear about us?')
    member_expiry_date = models.DateField(blank=True,null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.member_name

    def save(self, *args, **kwargs):
        for field_name in ['member_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())
        super(Member, self).save(*args, **kwargs)

    @property
    def is_expired(self):
        if self.member_expiry_date < date.today():
            return True
        return False


    def get_absolute_url(self):
        return reverse('member-detail',args=[str(self.id)] )
"""
Function to build
1. create user when saving and link to member id
2. update expiry date based on payment date
3. display expiring records (within one month?)

"""
class Car(models.Model):
    PRIMARY_SEC_CHOICES = (
        (1,'Primary'),
        (2,'Secondary'),
        )
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    car_reg_no = models.CharField(max_length=20, verbose_name='Registration Number')
    car_model = models.CharField(max_length=20, verbose_name='Model')
    car_engine_chasis = models.CharField(max_length=20, verbose_name='Engine Chassis',blank=True,null=True)
    car_primary_sec = models.SmallIntegerField(blank=True,null=True,choices=PRIMARY_SEC_CHOICES, verbose_name='Primary/Secondary Car')
    car_status = models.BooleanField(default=True,verbose_name='Status')
    def __str__(self):
        return self.car_reg_no
    #def get_absolute_url(self):
    #    return reverse('pcmapp:index')
    def save(self, *args, **kwargs):
        for field_name in ['car_reg_no','car_model','car_engine_chasis']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())
        for field_name in ['car_reg_no']:
            val =  getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.replace(" ",""))
        super(Car, self).save(*args, **kwargs)
"""
define secondary car insert
"""
class Payment(models.Model):
    PAYMENT_CHOICES= (
        ('1','New'),
        ('2','Renewal'),
        ('3','Supplementary'),
        )
    payment_car_reg_no = models.ForeignKey(Member,on_delete=models.CASCADE)
    payment_date = models.DateField(blank=True,verbose_name='Payment Date')
    payment_amount = models.IntegerField(verbose_name='Payment Amount')
    payment_type = models.CharField(max_length=1,choices = PAYMENT_CHOICES,verbose_name='Payment For')
    payment_receipt_image = models.FileField(upload_to='uploadreceipt',null=True,blank=True,verbose_name='Proof of Payment')
"""
update the expiry date when payment is made.
"""
