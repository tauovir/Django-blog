# Generated by Django 3.0.4 on 2020-05-09 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApi', '0002_question_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paradigm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('languages', models.ManyToManyField(to='webApi.Language')),
            ],
        ),
        migrations.AddField(
            model_name='language',
            name='paradigm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webApi.Paradigm'),
        ),
    ]
