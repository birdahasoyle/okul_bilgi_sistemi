# Generated by Django 3.1.7 on 2021-03-29 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kayit_islemleri', '0002_auto_20210329_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sehir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sehir_adi', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='okul',
            name='sehir',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kayit_islemleri.sehir', verbose_name='Sehir'),
        ),
    ]