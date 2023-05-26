# Generated by Django 4.1.7 on 2023-04-24 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_remove_post_category_remove_post_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=512)),
                ('photo', models.ImageField(upload_to='media/img')),
                ('contacts', models.CharField(max_length=15)),
                ('price', models.IntegerField()),
                ('publicationDate', models.DateTimeField()),
                ('rating', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]