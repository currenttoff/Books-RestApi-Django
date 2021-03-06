# Generated by Django 4.0.4 on 2022-06-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_product_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='b', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(default='fiction', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='book',
            name='stars',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='a', max_length=200),
        ),
    ]
