# Generated by Django 3.2.8 on 2021-11-13 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=10)),
                ('s_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=50)),
                ('batch_no', models.CharField(max_length=50)),
                ('companies_count', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
