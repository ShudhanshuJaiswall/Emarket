# Generated by Django 3.2.3 on 2021-06-04 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('userEmail', models.CharField(max_length=100)),
                ('userPhone', models.CharField(max_length=100, null=True)),
                ('userPass', models.CharField(max_length=10)),
                ('userPic', models.CharField(max_length=200, null=True)),
                ('userAddress', models.CharField(max_length=500, null=True)),
                ('otp', models.IntegerField()),
                ('isverify', models.BooleanField(default=False)),
            ],
        ),
    ]
