# Generated by Django 2.0.4 on 2018-05-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcmapp', '0013_auto_20180508_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_on_chat',
            field=models.BooleanField(choices=[('True', 'YES'), ('False', 'NO')], default='True', max_length=1),
        ),
    ]
