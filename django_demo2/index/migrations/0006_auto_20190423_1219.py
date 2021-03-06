# Generated by Django 2.1.7 on 2019-04-23 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20190423_1208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': '出版社', 'verbose_name_plural': '出版社'},
        ),
        migrations.AlterField(
            model_name='book',
            name='publicate_date',
            field=models.DateField(verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, verbose_name='书籍名称'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.CharField(max_length=100, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='city',
            field=models.CharField(max_length=50, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=30, verbose_name='国家'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=30, verbose_name='出版社名称'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(verbose_name='网址'),
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
        migrations.AlterModelTable(
            name='publisher',
            table='publisher',
        ),
    ]
