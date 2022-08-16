# Generated by Django 4.1 on 2022-08-16 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='项目名称', max_length=20, unique=True, verbose_name='项目名称')),
                ('leader', models.CharField(help_text='项目负责人', max_length=10, verbose_name='项目负责人')),
                ('is_execute', models.BooleanField(default=True, help_text='是否启动项目', verbose_name='是否启动项目')),
                ('desc', models.TextField(blank=True, default='', help_text='项目描述信息', null=True, verbose_name='项目描述信息')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
            ],
            options={
                'db_table': 'tb_projects',
            },
        ),
    ]
