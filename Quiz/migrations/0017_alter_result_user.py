# Generated by Django 4.1.1 on 2022-09-23 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0016_alter_result_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='user',
            field=models.CharField(default='e4946cfb-2242-4a00-bdcc-ee2e2a85a678', max_length=36),
        ),
    ]