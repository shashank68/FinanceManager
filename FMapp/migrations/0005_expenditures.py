# Generated by Django 3.0.7 on 2020-06-18 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FMapp', '0004_loans'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Date', models.DateField()),
                ('Remarks', models.TextField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenditures', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
