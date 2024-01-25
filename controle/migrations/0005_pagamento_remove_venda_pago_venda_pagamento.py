# Generated by Django 5.0 on 2024-01-24 23:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0004_produto_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('valor', models.FloatField(default=1.0, verbose_name='Valor da Compra')),
                ('tipo', models.IntegerField(choices=[(1, 'Dinheiro'), (2, 'Pix'), (3, 'Débito'), (4, 'Crédito')], default=1, verbose_name='Tipo do Pagamento')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('dataAlteracao', models.DateTimeField(auto_now=True, verbose_name='Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
                'ordering': ['id', 'dataCadastro'],
            },
        ),
        migrations.RemoveField(
            model_name='venda',
            name='pago',
        ),
        migrations.AddField(
            model_name='venda',
            name='pagamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='controle.pagamento', verbose_name='Pagamento'),
        ),
    ]