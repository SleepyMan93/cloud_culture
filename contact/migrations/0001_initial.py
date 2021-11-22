# Generated by Django 3.2.9 on 2021-11-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('contact_email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
