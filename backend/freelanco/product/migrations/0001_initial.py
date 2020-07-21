# Generated by Django 3.0.3 on 2020-03-25 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('actual_cost', models.FloatField()),
                ('discounted_cost', models.FloatField(default=-1)),
                ('post_date', models.DateField(auto_now_add=True, null=True)),
                ('picture', models.ImageField(default='items/default.jpg', upload_to='items/uploads/% Y/% m/% d/')),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField(blank=True, null=True)),
                ('ordered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('ordered', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Item')),
            ],
        ),
    ]
