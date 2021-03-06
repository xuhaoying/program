# Generated by Django 2.1.7 on 2019-04-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_author_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='publicate_date',
            field=models.DateField(),
        ),
    ]
