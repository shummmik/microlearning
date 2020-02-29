# Generated by Django 3.0.3 on 2020-02-28 19:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('microlearning', '0002_auto_20200224_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='status',
        ),
        migrations.CreateModel(
            name='ArticleInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular article', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('new', 'New'), ('finished', 'Finished')], default='new', max_length=20)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='microlearning.Article')),
            ],
        ),
    ]
