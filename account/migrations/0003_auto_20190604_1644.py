# Generated by Django 2.0.13 on 2019-06-04 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='cert_date',
            field=models.DateField(null=True),
        ),
    ]
