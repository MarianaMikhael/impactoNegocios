# Generated by Django 2.2.3 on 2019-11-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0007_auto_20191111_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_contingencia',
            name='RTO_Contingencia',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='RTO Contingência'),
        ),
    ]
