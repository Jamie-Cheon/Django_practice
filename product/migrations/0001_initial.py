# Generated by Django 3.0.6 on 2020-05-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Product Name')),
                ('price', models.IntegerField(verbose_name='Product Price')),
                ('description', models.TextField(verbose_name='Product Description')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='Register Date')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
                'db_table': "Jamie's shop_Product",
            },
        ),
    ]