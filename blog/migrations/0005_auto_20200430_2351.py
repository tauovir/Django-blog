# Generated by Django 3.0.4 on 2020-04-30 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('message', models.TextField(max_length=800)),
                ('created_at', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]