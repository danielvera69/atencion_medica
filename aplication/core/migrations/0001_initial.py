# Generated by Django 4.2.16 on 2024-10-26 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre del Cargo')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción del Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='CategoriaExamen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Categoría')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción de la Categoría')),
            ],
            options={
                'verbose_name': 'Categoría de Examen',
                'verbose_name_plural': 'Categorías de Exámenes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True, verbose_name='Código del Diagnóstico')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción del Diagnóstico')),
                ('datos_adicionales', models.TextField(blank=True, null=True, verbose_name='Datos Adicionales')),
            ],
            options={
                'verbose_name': 'Diagnóstico',
                'verbose_name_plural': 'Diagnósticos',
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Especialidad')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción de la Especialidad')),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='MarcaMedicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Marca de Medicamento')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo de Medicamento',
                'verbose_name_plural': 'Tipos de Medicamentos',
            },
        ),
        migrations.CreateModel(
            name='TipoMedicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Tipo de Medicamento')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo de Medicamento',
                'verbose_name_plural': 'Tipos de Medicamentos',
            },
        ),
        migrations.CreateModel(
            name='TipoSangre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10, unique=True, verbose_name='Tipo de Sangre')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de Sangre',
                'verbose_name_plural': 'Tipos de Sangre',
            },
        ),
        migrations.CreateModel(
            name='TipoCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del Examen')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción del Examen')),
                ('valor_minimo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Valor Mínimo')),
                ('valor_maximo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Valor Máximo')),
                ('categoria_examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias_examen', to='core.categoriaexamen', verbose_name='Categoría del Examen')),
            ],
            options={
                'verbose_name': 'Tipo de Examen',
                'verbose_name_plural': 'Tipos de Exámenes',
                'ordering': ['categoria_examen', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Nombre del Medicamento')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción del Medicamento')),
                ('concentracion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Concentración del Medicamento')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Stock')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('comercial', models.BooleanField(default=True, verbose_name='Comercial')),
                ('marca_medicamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='marca_medicamentos', to='core.marcamedicamento', verbose_name='Marca')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tipos_medicamentos', to='core.tipomedicamento', verbose_name='Tipo de Medicamento')),
            ],
            options={
                'verbose_name': 'Medicamento',
                'verbose_name_plural': 'Medicamentos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombre del Empleado')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellido del Empleado')),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cédula')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Sueldo')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('latitud', models.FloatField(blank=True, null=True, verbose_name='Latitud')),
                ('longitud', models.FloatField(blank=True, null=True, verbose_name='Longitud')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='empleados/', verbose_name='Foto del Empleado')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cargos', to='core.cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cédula')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('direccion', models.CharField(max_length=10, unique=True, verbose_name='Direccion Trabajo')),
                ('latitud', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True, verbose_name='Latitud')),
                ('longitud', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True, verbose_name='Longitud')),
                ('codigoUnicoDoctor', models.CharField(max_length=20, unique=True, verbose_name='Código Único del Doctor')),
                ('telefonos', models.CharField(max_length=20, verbose_name='Teléfonos')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo')),
                ('horario_atencion', models.TextField(verbose_name='Horario de Atencion')),
                ('duracion_cita', models.IntegerField(default=30, verbose_name='Tiempo de Atencion(minutos)')),
                ('curriculum', models.FileField(blank=True, null=True, upload_to='curriculums/', verbose_name='Curriculum Vitae')),
                ('firmaDigital', models.ImageField(blank=True, null=True, upload_to='firmas/', verbose_name='Firma Digital')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='doctores/', verbose_name='Foto')),
                ('imagen_receta', models.ImageField(blank=True, null=True, upload_to='recetas/', verbose_name='Imagen para Recetas')),
                ('especialidad', models.ManyToManyField(related_name='especialidades', to='core.especialidad', verbose_name='Especialidades')),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctores',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cédula')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono(s)')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Sexo')),
                ('estado_civil', models.CharField(choices=[('S', 'Soltero'), ('C', 'Casado'), ('U', 'Union Libre'), ('D', 'Divorciado'), ('V', 'Viudo')], max_length=10, verbose_name='Estado Civil')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección Domiciliaria')),
                ('latitud', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True, verbose_name='Latitud')),
                ('longitud', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True, verbose_name='Longitud')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='pacientes/', verbose_name='Foto')),
                ('alergias', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alergias')),
                ('enfermedades_cronicas', models.CharField(blank=True, max_length=100, null=True, verbose_name='Enfermedades Crónicas')),
                ('medicacion_actual', models.CharField(blank=True, max_length=100, null=True, verbose_name='Medicación Actual')),
                ('cirugias_previas', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cirugías Previas')),
                ('antecedentes_personales', models.TextField(blank=True, null=True, verbose_name='Antecedentes Personales')),
                ('antecedentes_familiares', models.TextField(blank=True, null=True, verbose_name='Antecedentes Familiares')),
                ('tipo_sangre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tipos_sangre', to='core.tiposangre', verbose_name='Tipo de Sangre')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['apellidos'],
                'indexes': [models.Index(fields=['apellidos'], name='core_pacien_apellid_53b526_idx')],
            },
        ),
    ]
