# Generated by Django 2.1 on 2018-10-05 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Puntaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('clave', models.CharField(max_length=300)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('puntos', models.IntegerField()),
                ('codigo_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='puntaje',
            name='codigo_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Usuario'),
        ),
        migrations.AddField(
            model_name='puntaje',
            name='codigo_valor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Valor'),
        ),
    ]
