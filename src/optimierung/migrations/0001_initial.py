# Generated by Django 2.0.13 on 2019-07-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lehrerinKlasse', models.IntegerField()),
                ('tandeminKlasse', models.IntegerField()),
                ('partnerinKlasse', models.IntegerField()),
                ('lehrerwechsel', models.IntegerField()),
                ('sportunterricht', models.IntegerField()),
                ('lehrerminimum', models.IntegerField()),
                ('solver', models.CharField(choices=[('Xpress', 'Xpress'), ('Pyomo', 'Pyomo')], max_length=20)),
            ],
        ),
    ]
