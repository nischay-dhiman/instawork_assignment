# Generated by Django 4.0.6 on 2022-07-09 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=150)),
                ('assigned_role', models.IntegerField(choices=[(0, 'Regular'), (1, 'Admin')], default=1)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
