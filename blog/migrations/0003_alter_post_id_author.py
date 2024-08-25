# Generated by Django 5.1 on 2024-08-25 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_post_id_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to='blog.author'),
        ),
    ]
