# Generated by Django 5.0 on 2024-01-26 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0006_alter_pagamento_valor_alter_produto_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='pagamento',
        ),
        migrations.AddField(
            model_name='pagamento',
            name='venda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pagamentosVenda', to='controle.venda', verbose_name='Venda'),
        ),
    ]