# Generated by Django 4.2.6 on 2023-11-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbSubject',
            fields=[
                ('no', models.AutoField(db_comment='学科编号', primary_key=True, serialize=False)),
                ('name', models.CharField(db_comment='学科名称', max_length=50)),
                ('intro', models.CharField(db_comment='学科介绍', max_length=1000)),
                ('is_hot', models.IntegerField(db_comment='是不是热门学科')),
            ],
            options={
                'db_table': 'tb_subject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbTeacher',
            fields=[
                ('no', models.AutoField(db_comment='老师编号', primary_key=True, serialize=False)),
                ('name', models.CharField(db_comment='老师姓名', max_length=20)),
                ('sex', models.IntegerField(db_comment='老师性别')),
                ('birth', models.DateField(db_comment='出生日期')),
                ('intro', models.CharField(db_comment='老师介绍', max_length=1000)),
                ('photo', models.CharField(db_comment='老师照片', max_length=255)),
                ('gcount', models.IntegerField(db_comment='好评数')),
                ('bcount', models.IntegerField(db_comment='差评数')),
            ],
            options={
                'db_table': 'tb_teacher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('tel', models.CharField(max_length=20, verbose_name='手机号')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('last_visit', models.DateTimeField(null=True, verbose_name='最后登录时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'tb_user',
            },
        ),
    ]