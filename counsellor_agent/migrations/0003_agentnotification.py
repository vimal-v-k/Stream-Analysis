# Generated by Django 3.1.7 on 2021-03-03 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_auto_20210303_1109'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('counsellor_agent', '0002_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notified_at', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('counsellor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.scoremodel')),
            ],
        ),
    ]
