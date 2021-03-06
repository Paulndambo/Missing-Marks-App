# Generated by Django 3.1.7 on 2021-03-25 10:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademeicYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=500)),
                ('school', models.CharField(max_length=500)),
                ('offices', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=200, unique=True)),
                ('title', models.CharField(choices=[('Mr.', 'Mr.'), ('Dr.', 'Dr.'), ('Prof.', 'Prof.'), ('Ms.', 'Ms.')], max_length=30)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Binary', 'Binary'), ('I prefer not to say', 'I prefer not to say')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('postal_code', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('employment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('employment_type', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time')], max_length=200)),
                ('education_qualifications', models.TextField()),
                ('schools_attended', models.TextField()),
                ('places_worked', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_code', models.CharField(max_length=200, unique=True)),
                ('unit_title', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.department')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_code', models.CharField(max_length=200, unique_for_year=True)),
                ('semester_name', models.CharField(max_length=200)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.academeicyear')),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.department')),
            ],
        ),
        migrations.CreateModel(
            name='MissingMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('year_of_study', models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year'), ('Fifth Year', 'Fifth Year')], max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.department')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.lecturer')),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.programme')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.semester')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.unit')),
            ],
        ),
    ]
