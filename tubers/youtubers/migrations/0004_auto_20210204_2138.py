# Generated by Django 3.1.4 on 2021-02-04 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0003_auto_20210103_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('code', 'code'), ('mobile_review', 'mobile_review'), ('vlogs', 'vlogs'), ('comedy', 'comedy'), ('gaming', 'gaming'), ('film_making', 'film_making'), ('cooking', 'cooking'), ('music', 'music'), ('motivation', 'motivation'), ('Body-Building', 'Body-Building')], max_length=255),
        ),
    ]
