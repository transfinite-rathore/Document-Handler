# Generated by Django 4.2.3 on 2023-07-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
