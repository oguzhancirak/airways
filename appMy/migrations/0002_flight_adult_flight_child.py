# Generated by Django 4.1.7 on 2023-05-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='adult',
            field=models.IntegerField(null=True, verbose_name='Yeşkin sayısı'),
        ),
        migrations.AddField(
            model_name='flight',
            name='child',
            field=models.IntegerField(null=True, verbose_name='Cocuk sayısı'),
        ),
    ]
