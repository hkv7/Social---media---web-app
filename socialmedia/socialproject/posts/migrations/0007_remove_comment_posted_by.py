# Generated by Django 5.0.6 on 2024-07-20 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_comment_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='posted_by',
        ),
    ]
