# Generated by Django 4.2.7 on 2024-05-15 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='19', on_delete=django.db.models.deletion.PROTECT, related_name='products', to='main.category'),
        ),
    ]
