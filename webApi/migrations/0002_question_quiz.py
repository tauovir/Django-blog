# Generated by Django 3.0.4 on 2020-05-04 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, verbose_name='description')),
                ('created_date', models.DateField(auto_now=True)),
                ('url', models.URLField(null=True, verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='question')),
                ('choice1', models.TextField(verbose_name='choice1')),
                ('choice2', models.TextField(verbose_name='choice2')),
                ('choice3', models.TextField(verbose_name='choice3')),
                ('choice4', models.TextField(verbose_name='choice4')),
                ('answer', models.CharField(max_length=10)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webApi.Quiz')),
            ],
        ),
    ]
