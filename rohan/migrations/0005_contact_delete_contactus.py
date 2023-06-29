# Generated by Django 4.2 on 2023-06-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rohan', '0004_rename_phone_contactus_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=10)),
                ('phonenumber', models.CharField(max_length=12)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='ContactUs',
        ),
    ]
