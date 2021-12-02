# Generated by Django 3.2.9 on 2021-12-02 13:02

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('softdeletablemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shared.softdeletablemodel')),
                ('path', models.CharField(max_length=150)),
                ('caption', models.TextField()),
                ('file', models.ImageField(upload_to='data_images/')),
            ],
            bases=('shared.softdeletablemodel',),
            managers=[
                ('non_deleted_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
