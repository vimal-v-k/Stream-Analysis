# Generated by Django 3.1.7 on 2021-03-02 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_studentdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccounts',
            old_name='is_councellor',
            new_name='is_counsellor',
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.useraccounts'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CounsellorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
