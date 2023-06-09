# Generated by Django 3.2.13 on 2023-02-07 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_isim', models.CharField(max_length=100)),
                ('kategori_resim', models.FileField(blank=True, null=True, upload_to='resim/', verbose_name='resimler')),
            ],
        ),
        migrations.CreateModel(
            name='resim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim1', models.ImageField(blank=True, null=True, upload_to='resim/')),
            ],
        ),
    ]
