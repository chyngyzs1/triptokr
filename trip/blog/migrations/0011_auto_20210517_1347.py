# Generated by Django 3.2.3 on 2021-05-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210517_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tours',
            name='sorting',
        ),
        migrations.AlterField(
            model_name='tours',
            name='category',
            field=models.CharField(choices=[('mountains', 'MOUNTAINS'), ('lakesAndRivers', 'LAKES AND RIVERS'), ('Gorges', 'GORGES'), ('waterfalls', 'WATERFALLS'), ('hotSpings', 'HOT SPRINGS'), ('equestrian', 'EQUESTIAN'), ('cultural', 'CULTURAL'), ('season', 'SEASON'), ('extreme', 'EXTREME')], max_length=16),
        ),
    ]
