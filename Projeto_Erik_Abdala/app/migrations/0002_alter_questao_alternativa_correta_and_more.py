# Generated by Django 4.2.7 on 2023-11-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='alternativa_correta',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='questao',
            name='alternativa_submetida',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
