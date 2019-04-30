# Generated by Django 2.2 on 2019-04-30 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Car')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Image')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Price')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Review')),
            ],
        ),
    ]