# Generated by Django 4.1.1 on 2022-09-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0013_alter_result_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='user',
            field=models.CharField(default='8dd4b8c6-9477-4ae2-8658-5008f6c390ba', max_length=36),
        ),
    ]