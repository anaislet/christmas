# Generated by Django 4.2.7 on 2023-11-09 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0003_delete_gift'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True, null=True)),
                ('price', models.CharField(choices=[('Moins de 40 €', 'Price1'), ('Entre 40 et 100 €', 'Price2'), ('Plus de 100€', 'Price3')], max_length=20)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.member')),
            ],
        ),
    ]
