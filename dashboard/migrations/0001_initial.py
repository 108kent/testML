# Generated by Django 3.0.2 on 2023-01-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('sex', models.PositiveIntegerField(choices=[(0, 'Female'), (1, 'Male')], null=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('year_in_germany', models.PositiveIntegerField(null=True)),
                ('predictions', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
