# Generated by Django 4.1.7 on 2023-05-07 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdsapp', '0006_bid2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usermail', models.CharField(max_length=50, unique=True)),
                ('userfeedback', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'contact_table',
            },
        ),
        migrations.AlterField(
            model_name='bid1',
            name='bidamount',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bid2',
            name='bidamount',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
