# Generated by Django 4.1.7 on 2023-06-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0008_alter_cor_options_alter_veiculo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='acessorios',
            field=models.ManyToManyField(related_name='veiculos', to='garagem.acessorio'),
        ),
    ]