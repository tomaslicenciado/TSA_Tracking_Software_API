# Generated by Django 3.2.6 on 2021-11-08 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Users', '0002_user_is_leader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=255, verbose_name='Código')),
                ('software_name', models.CharField(max_length=255, verbose_name='Nombre de software')),
                ('software_version', models.CharField(max_length=100, verbose_name='Versión de software')),
                ('active', models.BooleanField(default=True, verbose_name='Estado')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.client')),
                ('owner', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.SmallIntegerField(choices=[(0, 'Nuevo'), (1, 'En progreso'), (2, 'En revisión'), (3, 'En espera'), (4, 'Cerrado')], default=0, verbose_name='Estado')),
                ('description', models.CharField(max_length=255, verbose_name='Descripción')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('area', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='Users.area')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='Projects.project', verbose_name='Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='TicketDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='Descripción')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('ticket', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='Projects.ticket', verbose_name='Ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
