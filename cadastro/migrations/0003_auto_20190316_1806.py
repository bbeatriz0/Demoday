# Generated by Django 2.1.7 on 2019-03-16 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20190313_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
