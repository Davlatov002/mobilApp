# Generated by Django 4.2.7 on 2023-11-25 18:48

from django.db import migrations, models
import user.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('surname', models.CharField(blank=True, max_length=250, null=True)),
                ('profile_image', models.TextField(blank=True, null=True)),
                ('referal_link', models.CharField(default=user.models.generate_random_string, editable=False, max_length=8, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('wallet_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_verified', models.IntegerField(blank=True, null=True)),
                ('is_archived', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
