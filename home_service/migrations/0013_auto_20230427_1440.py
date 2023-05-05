# Generated by Django 3.1.3 on 2023-04-27 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home_service.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_service', '0012_spares'),
    ]

    operations = [
        migrations.CreateModel(
            name='FID_Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=home_service.models.get_file_path)),
                ('description', models.TextField(max_length=500)),
                ('meta_title', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pcategory1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=home_service.models.get_file_path)),
                ('name', models.CharField(max_length=50)),
                ('pcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_service.pcategory')),
            ],
        ),
        migrations.RenameModel(
            old_name='Spares',
            new_name='FService_Category',
        ),
        migrations.AddField(
            model_name='service_man',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='service_man',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=home_service.models.get_file_path)),
                ('product_image1', models.ImageField(blank=True, null=True, upload_to=home_service.models.get_file_path)),
                ('product_image2', models.ImageField(blank=True, null=True, upload_to=home_service.models.get_file_path)),
                ('small_description', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_service.pcategory1')),
            ],
        ),
        migrations.CreateModel(
            name='Fuel_man',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('id_type', models.CharField(max_length=100, null=True)),
                ('service_name', models.CharField(max_length=100, null=True)),
                ('id_card', models.FileField(null=True, upload_to='')),
                ('image', models.FileField(null=True, upload_to='')),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home_service.city')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home_service.fstatus')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_status', models.CharField(max_length=100, null=True)),
                ('vehicle_no', models.CharField(max_length=100, null=True)),
                ('book_days', models.CharField(max_length=100, null=True)),
                ('book_hours', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home_service.customer')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home_service.fuel_man')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home_service.fstatus')),
            ],
        ),
    ]
