# Generated by Django 2.0 on 2020-04-08 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('shared_name', models.CharField(blank=True, max_length=200)),
                ('cnpj', models.CharField(max_length=19, unique=True)),
                ('landline_1', models.CharField(db_index=True, max_length=22)),
                ('has_cx_priority', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='loggiuser',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='players.Company'),
        ),
    ]
