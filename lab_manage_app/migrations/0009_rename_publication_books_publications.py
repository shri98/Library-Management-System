# Generated by Django 4.0.5 on 2022-06-08 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_manage_app', '0008_delete_usersss_alter_books_table_alter_users_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='publication',
            new_name='publications',
        ),
    ]