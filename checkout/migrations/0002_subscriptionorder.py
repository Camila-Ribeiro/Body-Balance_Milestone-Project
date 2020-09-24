# Generated by Django 3.1.1 on 2020-09-24 20:29

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('plan_name', autoslug.fields.AutoSlugField(editable=False, populate_from='plan_duration')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscription_order', to='user_profile.userprofile')),
            ],
        ),
    ]
