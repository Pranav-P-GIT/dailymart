# Generated by Django 4.1.7 on 2023-02-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('img', models.ImageField(upload_to='pic')),
                ('disc', models.TextField()),
                ('discount', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
