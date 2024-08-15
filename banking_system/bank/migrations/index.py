from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('bank', 'previous_migration_name'),  # Replace with the actual previous migration name
    ]

    operations = [
        migrations.AddIndex(
            model_name='bankaccount',
            index=models.Index(fields=['balance'], name='balance_idx'),
        ),
    ]
