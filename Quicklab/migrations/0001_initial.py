# Generated by Django 4.0.6 on 2022-10-09 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('instructions', models.TextField(blank=True, max_length=255)),
                ('subject', models.CharField(choices=[('Physics', 'Physics'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry')], max_length=20)),
                ('level', models.CharField(choices=[('Form1', 'Form1'), ('Form 2', 'Form2'), ('Form 3', 'Form3'), ('Form 4', 'Form4')], max_length=10)),
                ('status', models.CharField(choices=[('DONE', 'Done'), ('Pending', 'Pending'), ('Not done', 'Not done')], max_length=15)),
                ('comments', models.BooleanField(default=False)),
                ('video', models.FileField(upload_to='')),
                ('observation', models.TextField(blank=True, max_length=255, null=True)),
                ('time_date', models.DateTimeField(auto_now_add=True)),
                ('comment_description', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=8)),
                ('level', models.CharField(choices=[('Form1', 'Form1'), ('Form 2', 'Form2'), ('Form 3', 'Form3'), ('Form 4', 'Form4')], max_length=10)),
                ('no_of_practicals', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('subject', models.CharField(choices=[('Physics', 'Physics'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=8)),
                ('practicals', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Teacher_practical', to='Quicklab.practical')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Teacher_student', to='Quicklab.student')),
            ],
        ),
        migrations.AddField(
            model_name='practical',
            name='tools',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tool_practical', to='Quicklab.tool'),
        ),
    ]
