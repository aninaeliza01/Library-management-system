# Generated by Django 5.0.6 on 2024-06-04 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_address', models.CharField(max_length=255)),
                ('aadhar_card_no', models.CharField(max_length=12)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('membership_type', models.CharField(choices=[('six_months', 'Six Months'), ('one_year', 'One Year'), ('two_years', 'Two Years')], max_length=20)),
            ],
        ),
    ]
