# Generated by Django 2.0.5 on 2018-06-02 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(blank=True, max_length=50)),
                ('Deadline', models.DateTimeField()),
                ('Status', models.BooleanField()),
                ('Number', models.IntegerField(default=0)),
            ],
        ),
    ]
