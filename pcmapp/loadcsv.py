import csv
import os


file = '/home/vignesk70/pcm/pcmapp/20180514_PCM SC Buddy_fixed_2.csv'

from pcmapp.models import Member,Car,Payment

with open(file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Member(member_name=row['member_name'], member_email=row['member_email'],member_since=row['member_since'], member_phone=row['member_phone'],member_on_chat=row['member_on_chat'].capitalize(),member_source=row['member_source'],member_expiry_date=row['member_expiry_date'])
        p.save()
        print(p.id)
        q = Car(member_id=Member.objects.get(pk=p.id),car_reg_no=row['car_reg_no'],car_model=row['car_model'],car_engine_chasis=row['car_engine_chasis'],car_primary_sec=1,car_status=True)
        q.save()
        r = Payment(payment_car_reg_no=Member.objects.get(pk=p.id),payment_date=row['payment_date'],payment_amount=row['payment_amount'],payment_type=row['payment_type'])
        r.save()

from django.contrib.auth.models import User,group

#member_name,member_email,member_phone,member_since,member_birthdate,member_address_state,member_address_postcode,member_on_chat,member_source,member_expiry_date
#car_reg_no,car_model,car_engine_chasis,car_primary_sec,car_status
#payment_date,payment_amount,payment_type
