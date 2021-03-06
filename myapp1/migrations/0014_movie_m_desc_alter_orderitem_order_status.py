# Generated by Django 4.0.3 on 2022-04-03 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0013_rename_order_item_orderitem_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='m_desc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order_status',
            field=models.CharField(choices=[('0', 'Cancelled Order'), ('1', 'Placed Order'), ('2', 'Sent Mail'), ('3', 'Activated Link')], default='1', max_length=20),
        ),
    ]
