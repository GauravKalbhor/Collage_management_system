# Generated by Django 5.0.1 on 2024-02-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_stu_formdetails_stu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu_formdetails',
            name='stu_image',
            field=models.ImageField(blank=True, null=True, upload_to='filepath'),
        ),
    ]
