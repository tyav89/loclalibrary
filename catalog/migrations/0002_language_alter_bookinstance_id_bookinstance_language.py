# Generated by Django 4.2.6 on 2023-10-12 11:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9d13d919-90e0-47f8-a3b9-70eb76167bef'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language'),
        ),
    ]
