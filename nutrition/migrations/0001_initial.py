# Generated by Django 3.1.1 on 2020-09-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('day', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('breakfast', models.TextField(max_length=1000)),
                ('am_snack', models.TextField(max_length=1000)),
                ('lunch', models.TextField(max_length=1000)),
                ('pm_snack', models.TextField(max_length=1000)),
                ('dinner', models.TextField(max_length=1000)),
                ('daily_total_cal', models.DecimalField(decimal_places=3, max_digits=4)),
                ('protein', models.CharField(max_length=100)),
                ('carbohydrates', models.CharField(max_length=100)),
                ('fiber', models.CharField(max_length=100)),
                ('fat', models.CharField(max_length=100)),
                ('sodium', models.DecimalField(decimal_places=3, max_digits=4)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image_file', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Nutrition',
            },
        ),
    ]
