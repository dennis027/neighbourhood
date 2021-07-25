# Generated by Django 3.2.5 on 2021-07-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourapp', '0005_rename_newpost_announce'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='votes_total',
        ),
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Announce',
        ),
    ]
