# Generated by Django 3.2.3 on 2021-05-16 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_tours_sorting'),
    ]

    operations = [
        migrations.AddField(
            model_name='tours',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
