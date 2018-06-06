# Generated by Django 2.0.4 on 2018-06-03 12:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='artice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('shjian', models.CharField(max_length=50)),
                ('zhaiyao', models.CharField(max_length=300)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='python',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ab', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserMssge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='zhuce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
