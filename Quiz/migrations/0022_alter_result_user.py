# Generated by Django 4.1.1 on 2022-10-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0021_alter_result_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='user',
            field=models.CharField(default='dbb5acc9-6d23-4ca1-b848-dbb554aa498c', max_length=36),
        ),
    ]