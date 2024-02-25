# Generated by Django 5.0.1 on 2024-02-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stu_FormDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_ID', models.CharField(max_length=100)),
                ('stu_Name', models.CharField(max_length=100)),
                ('stu_FaName', models.CharField(max_length=100)),
                ('stu_DOB', models.DateField(null=True)),
                ('stu_DOBjob', models.DateField(null=True)),
                ('stu_Add', models.CharField(max_length=100)),
                ('stu_Email', models.EmailField(max_length=100)),
                ('stu_Mobile', models.IntegerField()),
                ('stu_EmMobile', models.IntegerField()),
                ('stu_Adhar', models.CharField(max_length=12)),
                ('stu_Gender', models.CharField(max_length=10)),
                ('stu_Graduation', models.CharField(max_length=50)),
                ('stu_Branch', models.CharField(max_length=50)),
                ('stu_Collage', models.CharField(max_length=100)),
                ('stu_Department', models.CharField(max_length=50)),
                ('stu_Course', models.CharField(max_length=50)),
                ('stu_Course_Fee', models.IntegerField(null=True)),
                ('stu_image', models.ImageField(upload_to='uploads/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Teach_FormDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teach_ID', models.CharField(max_length=100)),
                ('teach_jtitle', models.CharField(max_length=100)),
                ('teach_Name', models.CharField(max_length=100)),
                ('teach_DOB', models.DateField(null=True)),
                ('teach_DOBjob', models.DateField(null=True)),
                ('teach_Department', models.CharField(max_length=50)),
                ('teach_Course', models.CharField(max_length=50)),
                ('teach_FaName', models.CharField(max_length=50)),
                ('teach_Email', models.EmailField(max_length=100)),
                ('teach_Mobile', models.IntegerField()),
                ('teach_EmMobile', models.IntegerField()),
                ('teach_Graduation', models.CharField(max_length=50)),
                ('teach_Postgraduation', models.CharField(max_length=50)),
                ('teach_Adhar', models.CharField(max_length=12)),
                ('teach_Add', models.CharField(max_length=100)),
                ('teach_Gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Stu_Details',
        ),
    ]