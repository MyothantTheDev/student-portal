# Generated by Django 4.1.1 on 2022-09-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0017_alter_result_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='user',
            field=models.CharField(default='7ebe20a2-8bde-4980-b235-0ae40e6409ed', max_length=36),
        ),
    ]
