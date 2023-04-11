# Generated by Django 2.2.28 on 2023-04-11 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_auto_20230411_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('groupID', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='usertype',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usertype',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='usertype',
            name='mobile',
        ),
        migrations.AddField(
            model_name='usertype',
            name='type_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('status', models.BooleanField(blank=True, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('dateUpdated', models.DateTimeField(blank=True, null=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings_userID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('status', models.BooleanField()),
                ('objectID', models.IntegerField()),
                ('roleID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permissions_roleID', to='home.Roles')),
                ('userID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permissions_userID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('roleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups_roleID', to='home.Roles')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups_userID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kpi_name', models.TextField()),
                ('kpi_value', models.TextField()),
                ('bookingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_bookingID', to='home.Bookings')),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_eventID', to='home.Events')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_userID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
