# Generated by Django 4.0.5 on 2022-06-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_manage_app', '0004_remove_users_id_alter_users_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]