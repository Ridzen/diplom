# Generated by Django 4.0.6 on 2022-08-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0003_heroesskills_image_first_heroesskills_image_second_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroesskills',
            name='image_first',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='heroesskills',
            name='image_second',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='heroesskills',
            name='image_third',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
