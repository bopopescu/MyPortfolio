# Generated by Django 2.1.5 on 2019-02-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_img', models.ImageField(upload_to='myapp/static/')),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=20)),
                ('linkedin', models.URLField()),
                ('github', models.URLField()),
            ],
        ),
    ]
