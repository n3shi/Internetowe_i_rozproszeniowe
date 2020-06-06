# Generated by Django 3.0.6 on 2020-06-06 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('algorithm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file_calculate_time',
        ),
        migrations.RemoveField(
            model_name='file',
            name='file_path',
        ),
        migrations.RemoveField(
            model_name='file',
            name='file_result_path',
        ),
        migrations.RemoveField(
            model_name='file',
            name='file_result_result',
        ),
        migrations.RemoveField(
            model_name='file',
            name='user',
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_result_path', models.CharField(max_length=240)),
                ('file_result_result', models.IntegerField()),
                ('file_calculate_time', models.IntegerField()),
                ('file_path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algorithm.File')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]