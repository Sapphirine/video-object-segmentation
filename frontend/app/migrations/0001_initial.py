# Generated by Django 2.2.6 on 2019-11-19 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoname', models.CharField(max_length=30)),
                ('headFile', models.FileField(upload_to='./upload/')),
            ],
        ),
    ]
