# Generated by Django 3.2 on 2021-04-25 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('blog_body', models.CharField(max_length=15000)),
                ('image_url', models.URLField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.CharField(max_length=300)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_author', models.CharField(max_length=60)),
                ('comment_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_title', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapi.blog')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapi.tag')),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapi.blog')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapi.comment')),
            ],
        ),
    ]
