# Generated by Django 3.2.1 on 2021-05-19 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='db',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('col_name', models.CharField(default='null', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='db2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('intgr', models.IntegerField()),
                ('col2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_app.db')),
            ],
        ),
    ]
