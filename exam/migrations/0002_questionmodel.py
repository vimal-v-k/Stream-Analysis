# Generated by Django 3.1.7 on 2021-03-02 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=100)),
                ('option_one', models.CharField(max_length=100)),
                ('option_two', models.CharField(max_length=100)),
                ('option_three', models.CharField(max_length=100)),
                ('option_four', models.CharField(max_length=100)),
                ('main_stream', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exam.streammodel')),
                ('sub_stream', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='exam.substreammodel')),
            ],
        ),
    ]
