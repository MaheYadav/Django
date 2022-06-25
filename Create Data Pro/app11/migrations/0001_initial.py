# Generated by Django 2.2.3 on 2019-08-03 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producce',
            fields=[
                ('p_no', models.IntegerField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=30)),
                ('p_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('p_image', models.ImageField(upload_to='media')),
            ],
        ),
    ]