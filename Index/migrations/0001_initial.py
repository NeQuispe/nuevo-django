# Generated by Django 4.2.6 on 2023-11-01 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=250)),
                ('anio', models.IntegerField()),
            ],
        ),
    ]
