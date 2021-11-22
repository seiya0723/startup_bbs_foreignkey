# Generated by Django 3.1.2 on 2021-10-27 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_auto_20211027_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=2000, verbose_name='コメント')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.topic', verbose_name='リプライ対象のトピック')),
            ],
            options={
                'db_table': 'reply',
            },
        ),
    ]