# Generated by Django 4.0.3 on 2022-04-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0015_alter_post_status_delete_poststatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Published', 'Published'), ('Pending', 'Pending'), ('Draft', 'Draft')], default=('Draft', 'Draft'), max_length=50),
        ),
    ]
