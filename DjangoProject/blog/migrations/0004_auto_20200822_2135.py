# Generated by Django 3.0.8 on 2020-08-23 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='<a href="http://daringfireball.net/projects/markdown/syntax" target="_blank">Markdown syntax</a> allowed, but no raw HTML. Examples: **bold**, *italic*, indent 4 spaces for a code block. <a id=\'ref\'>Quick reference</a>'),
        ),
    ]