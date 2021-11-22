# Generated by Django 3.1.2 on 2021-10-27 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='カテゴリ名')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bbs.category', verbose_name='カテゴリ'),
            preserve_default=False,
        ),
    ]
