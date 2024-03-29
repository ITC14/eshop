# Generated by Django 4.1.5 on 2023-01-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0006_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=35, null=True, unique=True),
        ),
    ]
