# Generated by Django 3.0.3 on 2020-03-05 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_blog_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.Category'),
        ),
    ]