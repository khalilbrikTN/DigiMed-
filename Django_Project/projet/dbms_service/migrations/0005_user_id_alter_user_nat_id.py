from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('dbms_service', '0004_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nat_id',
            field=models.CharField(max_length=14),
        ),
    ]
