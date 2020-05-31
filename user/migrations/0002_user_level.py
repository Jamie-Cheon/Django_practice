# Generated by Django 3.0.6 on 2020-05-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.CharField(choices=[('user', 'user'), ('admin', 'admin')], default='user', max_length=8, verbose_name='User level'),
            preserve_default=False,
        ),
    ]
