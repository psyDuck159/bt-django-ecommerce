# Generated by Django 4.0.3 on 2022-03-15 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.ImageField(default='images/icon-load-256x256.png', upload_to='images/')),
                ('description', models.TextField(blank=True, help_text='Short description for the product', max_length=1000, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.item')),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('XL', 'XL'), ('XXL', 'XXL')], default='M', max_length=3)),
            ],
            bases=('catalog.item',),
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.item')),
            ],
            bases=('catalog.item',),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.item')),
                ('cpu', models.CharField(blank=True, max_length=100, null=True)),
                ('ram', models.CharField(blank=True, choices=[('8', '8GB'), ('16', '16GB')], default='8', max_length=2, null=True)),
                ('storage', models.CharField(blank=True, choices=[('500', '500GB'), ('1000', '1TB')], default='500', max_length=10, null=True)),
            ],
            bases=('catalog.item',),
        ),
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.item')),
                ('cpu', models.CharField(blank=True, max_length=100, null=True)),
                ('ram', models.CharField(blank=True, choices=[('3', '3GB'), ('4', '4GB')], default='3', max_length=1, null=True)),
                ('storage', models.CharField(blank=True, choices=[('32', '32GB'), ('64', '64GB'), ('128', '128GB')], default='32', max_length=10, null=True)),
            ],
            bases=('catalog.item',),
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.item')),
                ('color', models.CharField(max_length=50)),
                ('size', models.PositiveIntegerField()),
            ],
            bases=('catalog.item',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.item')),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.ManyToManyField(to='catalog.author')),
            ],
            bases=('catalog.item',),
        ),
    ]
