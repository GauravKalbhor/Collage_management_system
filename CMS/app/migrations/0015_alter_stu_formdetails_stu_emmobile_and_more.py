# Generated by Django 5.0.1 on 2024-02-08 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_stu_formdetails_stu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu_formdetails',
            name='stu_EmMobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stu_formdetails',
            name='stu_Mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stu_formdetails',
            name='stu_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
