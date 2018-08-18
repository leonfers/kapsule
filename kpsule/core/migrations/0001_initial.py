# Generated by Django 2.1 on 2018-08-18 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Capsula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('descricao', models.CharField(max_length=200)),
                ('tempo_estimado', models.IntegerField()),
                ('tempo_gasto', models.IntegerField()),
                ('orcamento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('descricao', models.CharField(max_length=3000)),
                ('escopo', models.CharField(max_length=20000)),
                ('tempo_estimado', models.IntegerField()),
                ('orcamento', models.IntegerField()),
                ('un_tempo', models.CharField(choices=[('seg', 1), ('min', 60), ('h', 3600), ('d', 86400)], default='seg', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200)),
                ('custo', models.IntegerField()),
                ('quantidade', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SubProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('descricao', models.CharField(max_length=200)),
                ('tempo_estimado', models.IntegerField()),
                ('orcamento', models.IntegerField()),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Projeto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=400)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.AddField(
            model_name='projeto',
            name='proprietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Usuario'),
        ),
        migrations.AddField(
            model_name='capsula',
            name='recursos',
            field=models.ManyToManyField(to='core.Recurso'),
        ),
        migrations.AddField(
            model_name='capsula',
            name='subProduto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SubProduto'),
        ),
    ]