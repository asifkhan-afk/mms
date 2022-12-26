# Generated by Django 3.2.10 on 2022-12-26 06:02

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_sidefund_date_alter_student_admission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doners',
            name='month',
            field=models.PositiveIntegerField(default=12, validators=[app.validators.validate_date]),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.PositiveIntegerField(blank=True, default=26, null=True),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='month',
            field=models.PositiveIntegerField(default=12, validators=[app.validators.validate_date]),
        ),
        migrations.AlterField(
            model_name='monthrevenue',
            name='month',
            field=models.PositiveIntegerField(default=12, validators=[app.validators.validate_date]),
        ),
        migrations.AlterField(
            model_name='muqtadi',
            name='adm_month',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='muqtadi',
            name='admission_date',
            field=models.IntegerField(default=26, validators=[app.validators.validate_date]),
        ),
        migrations.AlterField(
            model_name='salreciver',
            name='month',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='sidefund',
            name='date',
            field=models.PositiveIntegerField(blank=True, default=26, null=True),
        ),
        migrations.AlterField(
            model_name='sidefund',
            name='month',
            field=models.PositiveIntegerField(blank=True, default=12, null=True, validators=[app.validators.validate_date]),
        ),
        migrations.AlterField(
            model_name='student',
            name='adm_month',
            field=models.PositiveIntegerField(default=12, validators=[app.validators.validate_date]),
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_date',
            field=models.PositiveIntegerField(default=26, validators=[app.validators.validate_date]),
        ),
        migrations.AlterField(
            model_name='studoners',
            name='month',
            field=models.PositiveIntegerField(default=12, validators=[app.validators.validate_date]),
        ),
        migrations.AlterField(
            model_name='teachdoner',
            name='month',
            field=models.PositiveIntegerField(default=12, validators=[app.validators.validate_date]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='adm_month',
            field=models.IntegerField(default=12, validators=[app.validators.validate_date]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='admission_date',
            field=models.IntegerField(default=26, validators=[app.validators.validate_date]),
        ),
    ]