# Generated by Django 4.2.7 on 2023-11-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('fecha', models.DateField()),
                ('nombre_especialista', models.CharField(max_length=100)),
                ('diagnostico', models.TextField()),
                ('procedimiento', models.TextField()),
                ('tratamiento', models.TextField()),
                ('paciente_id', models.IntegerField()),
            ],
        ),
    ]