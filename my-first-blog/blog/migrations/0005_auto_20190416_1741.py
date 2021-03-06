# Generated by Django 2.1.7 on 2019-04-16 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190416_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='kolvo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=70)),
                ('title', models.CharField(max_length=70)),
                ('content', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.FileField(blank=True, upload_to='')),
                ('edinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.kolvo')),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='number',
            field=models.CharField(max_length=50),
        ),
    ]
