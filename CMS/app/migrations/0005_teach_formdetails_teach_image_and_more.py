# Generated by Django 5.0.1 on 2024-02-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_stu_formdetails_stu_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teach_formdetails',
            name='teach_image',
            field=models.ImageField(null=True, upload_to='uploads/images/'),
        ),
        migrations.AddField(
            model_name='teach_formdetails',
            name='teach_salary',
            field=models.IntegerField(null=True),
        ),
    ]