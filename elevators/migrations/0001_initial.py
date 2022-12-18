# Generated by Django 4.0.6 on 2022-12-18 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_floor', models.PositiveIntegerField()),
                ('direction', models.CharField(max_length=5)),
                ('maintenance_status', models.CharField(max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.PositiveIntegerField()),
                ('direction', models.CharField(max_length=5)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('elevator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elevators.elevator')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('elevator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='elevators.elevator')),
            ],
        ),
    ]
