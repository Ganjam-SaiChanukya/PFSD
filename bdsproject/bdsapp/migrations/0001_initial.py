# Generated by Django 4.1.7 on 2023-04-01 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Others', 'Prefer not to say')], max_length=10)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField(unique=True)),
                ('registrationtime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'registration_table',
            },
        ),
    ]
