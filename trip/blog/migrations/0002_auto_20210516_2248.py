# Generated by Django 3.2.3 on 2021-05-16 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('body', models.TextField()),
                ('price', models.IntegerField()),
                ('date', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=30)),
                ('point', models.FloatField()),
                ('img', models.ImageField(upload_to='uploads/', verbose_name='image')),
            ],
        ),
        migrations.AlterModelOptions(
            name='sendmess',
            options={'verbose_name': 'message', 'verbose_name_plural': 'messages'},
        ),
    ]
