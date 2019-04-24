# Generated by Django 2.1.7 on 2019-04-24 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_wife'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wife',
            options={'verbose_name': '夫人', 'verbose_name_plural': '夫人'},
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=None, to='index.Publisher'),
        ),
        migrations.AlterField(
            model_name='wife',
            name='author',
            field=models.OneToOneField(on_delete=None, to='index.Author', verbose_name='丈夫'),
        ),
        migrations.AlterField(
            model_name='wife',
            name='wage',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='wife',
            name='wname',
            field=models.CharField(max_length=30, verbose_name='姓名'),
        ),
    ]
