import csv
import os


file = '/home/vignesk70/pcm/pcmapp/20180514_PCM SC Buddy_fixed_1.csv'

from pcmapp.models import Member,Car

with open(file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Member(member_name=row['member_name'], member_email=row['member_email'],member_since=row['member_since'], member_phone=row['member_phone'],member_on_chat=row['member_on_chat'].capitalize(),member_source=row['member_source'],member_expiry_date=row['member_expiry_date'])
        #q = Car(car_reg_no=row['car_reg_no'],car_model=row['car_model'],car_engine_chasis=['car_engine_chasis'],car_primary_sec=1,car_status=True)
        print(p)
       # print(q)
        p.save()
       # q.save()

with open(file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #p = Member(member_name=row['member_name'], member_email=row['member_email'],member_since=row['member_since'], member_phone=row['member_phone'],member_on_chat=row['member_on_chat'].capitalize(),member_source=row['member_source'],member_expiry_date=row['member_expiry_date'])
        q = Car(car_reg_no=row['car_reg_no'],car_model=row['car_model'],car_engine_chasis=['car_engine_chasis'],car_primary_sec=1,car_status=True)
       # print(p)
        print(q)
       # p.save()
        q.save()
#member_name,member_email,member_phone,member_since,member_birthdate,member_address_state,member_address_postcode,member_on_chat,member_source,member_expiry_date
#car_reg_no,car_model,car_engine_chasis,car_primary_sec,car_status