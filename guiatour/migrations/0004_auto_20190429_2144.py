# Generated by Django 2.2 on 2019-04-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guiatour', '0003_auto_20190429_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guia',
            name='sexo',
            field=models.CharField(choices=[('Mas', 'Masculino'), ('Fem', 'Fenenino')], max_length=100),
        ),
    ]