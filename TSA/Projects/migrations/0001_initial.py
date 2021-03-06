# Generated by Django 3.2.6 on 2021-11-15 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.SmallIntegerField(choices=[(0, 'Nuevo'), (1, 'En progreso'), (2, 'En revisión'), (3, 'En espera'), (4, 'Cerrado')], default=0, verbose_name='Estado')),
                ('description', models.CharField(max_length=255, verbose_name='Descripción')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('area', models.SmallIntegerField(choices=[(0, 'Project Management'), (1, 'Sales'), (2, 'Requirements'), (3, 'User Experience'), (4, 'Development'), (5, 'Quality Assurance'), (6, 'Testing'), (7, 'Maintenance')], default=0, verbose_name='Area')),
            ],
        ),
        migrations.CreateModel(
            name='TicketDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='Descripción')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('ticket', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='Projects.ticket', verbose_name='Ticket')),
            ],
        ),
    ]
