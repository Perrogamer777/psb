# Generated by Django 4.2.1 on 2023-06-24 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='ciudadId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='soporte.ciudad'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='mensajeId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='soporte.tipomensaje'),
        ),
    ]
