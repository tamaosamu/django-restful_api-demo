# Generated by Django 4.2.7 on 2023-11-23 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_userext'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32)),
                ('brithday', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.DeleteModel(
            name='UserExt',
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Book',
        ),
        migrations.AddField(
            model_name='info',
            name='user',
            field=models.OneToOneField(db_column='uid', on_delete=django.db.models.deletion.CASCADE, related_query_name='user_id', to='module1.book'),
        ),
        migrations.AddField(
            model_name='article',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module1.book'),
        ),
    ]