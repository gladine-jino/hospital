# Generated by Django 4.1 on 2022-10-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_alter_productdetails_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='expiry',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
