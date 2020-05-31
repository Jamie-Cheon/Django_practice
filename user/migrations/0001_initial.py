# Generated by Django 3.0.6 on 2020-05-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=64, verbose_name='Password')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='Register Date')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
                'db_table': "Jamie's shop_user",
            },
        ),
    ]
