# Generated by Django 2.1.7 on 2019-04-03 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190401_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='estPublic',
            field=models.BooleanField(default=False, verbose_name='Public (cochez) ou Interne (décochez)'),
        ),
        migrations.AddField(
            model_name='projet',
            name='estPublic',
            field=models.BooleanField(default=False, verbose_name='Public (cochez) ou Interne (décochez)'),
        ),
    ]