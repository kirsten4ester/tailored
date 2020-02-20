# Generated by Django 3.0.3 on 2020-02-19 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=40)),
                ('category', models.CharField(default='no category', max_length=40)),
                ('price', models.CharField(default='', max_length=100)),
                ('photo_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shoot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default='no category', max_length=40)),
                ('photo_url', models.TextField()),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoots', to='tailored.Photographer')),
            ],
        ),
    ]
