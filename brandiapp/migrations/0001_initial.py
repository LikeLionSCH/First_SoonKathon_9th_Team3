# Generated by Django 3.2.5 on 2021-07-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('detail_image', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('product_name', models.CharField(max_length=100)),
                ('explanation', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('review_image', models.ImageField(blank=True, null=True, upload_to='review/')),
            ],
        ),
    ]
