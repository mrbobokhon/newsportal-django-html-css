# Generated by Django 3.2.5 on 2021-07-15 16:16

from django.db import migrations, models
import main.models
import newsportal.minixs


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_uz', models.CharField(max_length=100, verbose_name='Sarlavha (uz)')),
                ('subject_ru', models.CharField(max_length=100, verbose_name='Sarlavha (ru)')),
                ('content_uz', models.TextField(verbose_name='Izoh (uz)')),
                ('content_ru', models.TextField(verbose_name='Izoh (ru)')),
                ('image', models.ImageField(upload_to=main.models.posts_upload_to, verbose_name='img')),
                ('read', models.IntegerField(default=0)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            bases=(newsportal.minixs.TranslateMixin, models.Model),
        ),
    ]
