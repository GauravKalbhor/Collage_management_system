# Generated by Django 4.2.5 on 2024-02-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_delete_stu_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stu_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_ID', models.CharField(max_length=100)),
                ('stu_Name', models.CharField(max_length=100)),
                ('stu_FaName', models.CharField(max_length=100)),
                ('stu_DOB', models.DateField(auto_now=True)),
                ('stu_DOBjob', models.DateField(auto_now=True)),
                ('stu_Add', models.CharField(max_length=100)),
                ('stu_Email', models.EmailField(max_length=100)),
                ('stu_Mobile', models.IntegerField(max_length=99999999999)),
                ('stu_EmMobile', models.IntegerField(max_length=99999999999)),
                ('stu_Adhar', models.CharField(max_length=10)),
                ('stu_Gender', models.CharField(max_length=10)),
                ('stu_Graduation', models.CharField(max_length=10)),
                ('stu_Branch', models.CharField(max_length=10)),
                ('stu_Collage', models.CharField(max_length=10)),
                ('stu_Department', models.CharField(max_length=50)),
                ('stu_Course', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teach_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teach_ID', models.CharField(max_length=100)),
                ('teach_jtitle', models.CharField(max_length=100)),
                ('teach_Name', models.CharField(max_length=100)),
                ('teach_DOB', models.DateField(auto_now=True)),
                ('teach_DOBjob', models.DateField(auto_now=True)),
                ('teach_Department', models.CharField(max_length=10)),
                ('teach_Course', models.CharField(max_length=50)),
                ('teach_FaName', models.CharField(max_length=50)),
                ('teach_Email', models.EmailField(max_length=100)),
                ('teach_Mobile', models.IntegerField(max_length=99999999999)),
                ('teach_EmMobile', models.IntegerField(max_length=99999999999)),
                ('teach_Graduation', models.CharField(max_length=10)),
                ('teach_Postgraduation', models.CharField(max_length=10)),
                ('teach_Adhar', models.CharField(max_length=10)),
                ('teach_Add', models.CharField(max_length=10)),
                ('teach_Gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Stu_FormDetails',
        ),
        migrations.DeleteModel(
            name='Teach_FormDetails',
        ),
    ]