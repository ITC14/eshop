# Generated by Django 4.1.5 on 2023-01-28 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0013_arrival_arrival_details_arrival_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=30, unique=True)),
                ('payed_at', models.DateTimeField(auto_now=True)),
                ('mode', models.CharField(default='Liquidity', max_length=30)),
                ('details', models.TextField(blank=True, null=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='payment', to='eshop.order')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('price', models.FloatField(default=0)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('delivered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='eshop.myuser')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='deliveries', to='eshop.order')),
            ],
        ),
    ]
