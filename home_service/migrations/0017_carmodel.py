# Generated by Django 3.1.3 on 2023-05-01 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0016_delete_carmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carmodel', models.CharField(blank=True, max_length=150, null=True)),
                ('carbrand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_service.carbrand')),
            ],
        ),
    ]
