# Generated by Django 4.1.6 on 2023-02-06 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copycat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mp4file',
            name='text',
        ),
        migrations.AddField(
            model_name='mp4file',
            name='file',
            field=models.FileField(default=0, upload_to='media/'),
            preserve_default=False,
        ),
    ]
