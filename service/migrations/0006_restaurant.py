# Generated by Django 2.0.4 on 2018-08-11 16:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20180811_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_name', models.CharField(max_length=100, unique=True)),
                ('cons_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date added')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.category')),
            ],
        ),
    ]