# Generated by Django 3.2.5 on 2021-07-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourapp', '0007_user_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=29)),
                ('pic', models.ImageField(default='woman.png', upload_to='images/')),
            ],
        ),
    ]
