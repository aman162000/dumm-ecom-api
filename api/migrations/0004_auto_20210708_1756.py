# Generated by Django 3.2.5 on 2021-07-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_category_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img_lg',
            field=models.ImageField(blank=True, upload_to='images/600/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img_md',
            field=models.ImageField(blank=True, upload_to='images/300/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img_sm',
            field=models.ImageField(blank=True, upload_to='images/150/'),
        ),
    ]
