# Generated by Django 4.0.5 on 2022-06-08 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_manage_app', '0010_rename_publications_books_publication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='id',
        ),
        migrations.AlterField(
            model_name='books',
            name='book_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
