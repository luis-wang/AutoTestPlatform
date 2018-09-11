# Generated by Django 2.0.5 on 2018-09-10 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('inChargeUser', models.IntegerField(max_length=4)),
                ('createUser', models.IntegerField(max_length=4)),
                ('createTime', models.DateField(auto_now=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
