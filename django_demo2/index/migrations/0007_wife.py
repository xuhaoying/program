# Generated by Django 2.1.7 on 2019-04-24 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20190423_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wname', models.CharField(max_length=30)),
                ('wage', models.IntegerField()),
                ('author', models.OneToOneField(on_delete=None, to='index.Author')),
            ],
            options={
                'db_table': 'wife',
            },
        ),
    ]
